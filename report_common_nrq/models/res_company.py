# -*- coding: utf-8 -*-
# Copyright 2016-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    company_name = fields.Char(
        "Company Name for Reports",
        translate=True,
    )
    company_name_alt = fields.Char(
        "Company Name for Reports (Alt.)",
        translate=True,
    )
    company_address = fields.Text(
        "Company Address for Reports",
        translate=True,
    )
    company_address_alt = fields.Text(
        "Company Address for Reports (Alt.)",
        translate=True,
    )
    bank_details = fields.Text(
        string="Bank Details",
        translate=True,
    )
    bank_details_alt = fields.Text(
        string="Bank Details (Alt.)",
        translate=True,
    )
    chop = fields.Binary(
        "Company Chop Image",
        attachment=True,
    )
    chop_alt = fields.Binary(
        "Company Chop Image (Alt.)",
        attachment=True,
    )
