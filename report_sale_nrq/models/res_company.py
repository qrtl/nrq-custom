# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    sale_remarks = fields.Text(
        string="Sales Remarks",
    )
