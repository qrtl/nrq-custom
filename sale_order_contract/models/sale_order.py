# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    contract = fields.Selection(
        [("cont", "Contract"), ("quasi", "Quasi-mandate")],
        string="Contract",
        required=True,
    )
