# -*- coding: utf-8 -*-
# Copyright 2016-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    company_name = fields.Char("Company Name for Reports", translate=True,)
    company_name_alt = fields.Char("Company Name for Reports (Alt.)", translate=True,)
    company_address = fields.Text("Address for Reports", translate=True,)
    company_address_alt = fields.Text("Address for Reports (Alt.)", translate=True,)
    company_phone = fields.Char("Phone for Reports", translate=True,)
    company_phone_alt = fields.Char("Phone for Reports (Alt.)", translate=True,)
    company_fax = fields.Char("Fax for Reports", translate=True,)
    company_fax_alt = fields.Char("Fax for Reports (Alt.)", translate=True,)
    company_website = fields.Char("Website for Reports",)
    company_website_alt = fields.Char("Website for Reports (Alt.)",)
    bank_details = fields.Text(string="Bank Details", translate=True,)
    bank_details_alt = fields.Text(string="Bank Details (Alt.)", translate=True,)
    chop = fields.Binary("Company Chop Image", attachment=True,)
    chop_alt = fields.Binary("Company Chop Image (Alt.)", attachment=True,)
    invoice_remarks = fields.Text(string="Invoice Remarks",)
