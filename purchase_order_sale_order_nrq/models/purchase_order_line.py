# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    sale_ids = fields.Many2many(
        'sale.order',
        compute="_compute_sale_ids",
        store=True,
        string='Related Sales Order(s)'
    )

    @api.multi
    @api.depends('account_analytic_id')
    def _compute_sale_ids(self):
        for order_line in self:
            if order_line.account_analytic_id:
                order_line.sale_ids = self.env["sale.order"].search([(
                    "project_id", "=", order_line.account_analytic_id.id)])
