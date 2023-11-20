# -*- coding: utf-8 -*-
# Copyright 2016-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    company_name = fields.Char("Company Name for Reports", translate=True,)
    company_address = fields.Text("Address for Reports", translate=True,)
    company_phone = fields.Char("Phone for Reports", translate=True,)
    company_fax = fields.Char("Fax for Reports", translate=True,)
    company_website = fields.Char("Website for Reports",)
    bank_details = fields.Text(string="Bank Details", translate=True,)
    chop = fields.Binary("Company Chop Image", attachment=True,)
    invoice_remarks = fields.Text(string="Invoice Remarks",)
