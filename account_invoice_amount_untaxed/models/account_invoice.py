# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    amount_untaxed_curr_signed = fields.Monetary(
        "Untaxed Amount in Transaction Currency",
        compute="_compute_amount_untaxed_curr_signed",
        currency_field="currency_id",
        store=True,
    )

    @api.multi
    @api.depends("amount_untaxed")
    def _compute_amount_untaxed_curr_signed(self):
        for invoice in self:
            sign = invoice.type in ['in_refund', 'out_refund'] and -1 or 1
            invoice.amount_untaxed_curr_signed = invoice.amount_untaxed * sign
