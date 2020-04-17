# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sale_ids = fields.Many2many(
        'sale.order',
        related='invoice_line_ids.sale_ids',
        string='Related Sales Order(s)'
    )
