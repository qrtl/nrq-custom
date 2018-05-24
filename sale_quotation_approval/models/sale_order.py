# -*- coding: utf-8 -*-
# Copyright 2017-2018 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval = fields.Boolean(
        string='Approved',
        readonly=True,
        default=False,
        copy=False,
        track_visibility='onchange',
    )
    approval_user_id = fields.Many2one(
        'res.users',
        string='Approver',
        readonly=True,
    )
    self_approval_permission = fields.Boolean(
        string='Self-approval Permission',
        default=False,
    )
    approval_availability = fields.Boolean(
        string='Approval Availability',
        compute='_compute_approval_availability',
    )

    @api.multi
    def write(self, vals):
        if 'state' in vals:
            for quote in self:
                if vals['state'] == "cancel":
                    vals['approval'] = False
                elif (quote.state == "draft" and quote.approval) or vals['state'] in ["sale", "done"]:
                    vals['approval'] = True
                elif quote.state != "draft":
                    vals['approval'] = False
        res = super(SaleOrder, self).write(vals)
        return res

    @api.multi
    def action_approve(self):
        for quote in self:
            quote.approval = True
            quote.approval_user_id = quote.env.user.id

    @api.multi
    def action_cancel_approval(self):
        for quote in self:
            quote.approval = False
            quote.approval_user_id = False

    @api.multi
    def _compute_approval_availability(self):
        for quote in self:
            quote.approval_availability = (quote.user_id != quote.env.user) \
                                          or quote.self_approval_permission
