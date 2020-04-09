# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


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
    # make the field editable when status is 'open'
    comment = fields.Text(
        states={'draft': [('readonly', False)],
                'proforma': [('readonly', False)],
                'proforma2': [('readonly', False)],
                'open': [('readonly', False)]}
    )


    @api.multi
    @api.depends('state')
    def _update_ready_to_validate(self):
        for inv in self:
            if inv.state != 'draft':
                inv.ready_to_validate == False

    @api.multi
    def action_invoice_ok(self):
        for inv in self:
            inv.ready_to_validate = True

    @api.multi
    def action_invoice_ng(self):
        for inv in self:
            inv.ready_to_validate = False
