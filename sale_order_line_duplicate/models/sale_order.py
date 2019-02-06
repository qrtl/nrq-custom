# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_duplicate_order_line(self):
        for order in self:
            order_lines = order.order_line
            for line in order_lines:
                default = {
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'product_uom_qty': line.product_uom_qty,
                    'price_unit': line.price_unit,
                    'order_id': order.id
                }
                line.copy(default=default)
