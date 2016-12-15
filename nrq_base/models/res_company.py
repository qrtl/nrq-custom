# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    chop = fields.Binary(
        "Company Chop Image",
        attachment=True,
    )
    bank_details = fields.Char(
        string="Bank Details",
        translate=True,
    )
