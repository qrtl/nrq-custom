# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    sale_ids = fields.Many2many(
        "sale.order", related="order_line.sale_ids", string="Related Sales Order(s)"
    )
