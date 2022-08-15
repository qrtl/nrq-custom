# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    partner_no = fields.Char(related="partner_id.partner_no", readonly=True, store=True)
