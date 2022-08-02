# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    is_company_curr = fields.Boolean("Is_Company_Currency",
        compute="_compute_is_company_curr",
        store=True,
    )
    
    @api.depends("company_currency_id")
    def _compute_is_company_curr(self):
        for invoice in self:
            invoice.is_company_curr = False
            if invoice.currency_id == invoice.company_currency_id:
                invoice.is_company_curr = True
