# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_ids = fields.Many2many(
        'sale.order',
        compute="_compute_sale_ids",
        store=True,
        string='Related Sales Order(s)'
    )

    @api.multi
    @api.depends('order_line')
    def _compute_sale_ids(self):
        for order in self:
            account_analytic_id_list = []
            for order_line in order.order_line:
                if order_line.account_analytic_id:
                    account_analytic_id_list.append(
                        order_line.account_analytic_id.id)
            if account_analytic_id_list:
                order.sale_ids = self.env["sale.order"].search([(
                    "project_id", "in", account_analytic_id_list)])
