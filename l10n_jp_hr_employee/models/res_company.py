# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    appointment_letter_url = fields.Char("Letter of Appointment Link(" "Dependant)")
    private_page_header_text = fields.Html("Private Page Header Text", sanitize=True)
