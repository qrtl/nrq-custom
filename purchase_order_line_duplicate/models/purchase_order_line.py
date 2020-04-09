# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.multi
    def action_duplicate_line(self):
        for line in self:
            default = {
                'product_id': line.product_id.id,
                'name': line.name,
                'product_uom': line.product_uom.id,
                'price_unit': line.price_unit,
                'product_qty': line.product_qty,
                'order_id': line.order_id.id
            }
            line.copy(default=default)
