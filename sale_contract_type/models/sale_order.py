# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    contract = fields.Selection(
        [
            ("cont", "Contract Agreement"),
            ("quasi", "Quasi-mandate"),
            ("temp", "Temporary"),
        ],
        string="Contract",
        required=True,
    )
