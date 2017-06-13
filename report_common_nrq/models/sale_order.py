# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    show_tax = fields.Boolean(
        string="Show Tax",
        help="Show tax in printed quotation."
    )
    doc_title = fields.Char(
        string="Doc Title",
    )

    approval = fields.Boolean(
        string='Approval',
        compute='_update_approve',
        store=True,
        readonly=True,
        default=False,
        copy=False,
    )

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({'doc_title': self.doc_title})
        return res

    @api.multi
    def write(self, vals):
        if 'state' in vals:
            for quotation in self:
                if quotation.state == "draft" and quotation.approval:
                    vals['approval'] = True
                elif quotation.state != "draft":
                    vals['approval'] = False
        res = super(SaleOrder, self).write(vals)
        return res

    @api.multi
    def action_approve(self):
        for inv in self:
            inv.approval = True

    @api.multi
    def action_disapprove(self):
        for inv in self:
            inv.approval = False