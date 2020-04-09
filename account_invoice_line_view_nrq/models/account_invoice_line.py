# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    commercial_partner_id = fields.Many2one(
        'res.partner',
        related='invoice_id.commercial_partner_id',
        string='Partner Company',
        store=True,
        readonly=True,
    )
    state = fields.Selection(
        related='invoice_id.state',
        string='Invoice Status',
        store=True
    )
