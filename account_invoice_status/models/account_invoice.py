# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    ready_to_validate = fields.Boolean(
        string='Ready to Validate',
        compute='_update_ready_to_validate',
        store=True,
        readonly=True,
        default=False,
        copy=False,
    )


    @api.multi
    @api.depends('state')
    def _update_ready_to_validate(self):
        for inv in self:
            if inv.state == 'open':
                inv.ready_to_validate == False

    @api.multi
    def action_invoice_ok(self):
        for inv in self:
            inv.ready_to_validate = True

    @api.multi
    def action_invoice_ng(self):
        for inv in self:
            inv.ready_to_validate = False
