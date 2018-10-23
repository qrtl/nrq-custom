# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sale_ids = fields.Many2many(
        'sale.order',
        compute="_compute_sale_ids",
        store=True,
        string='Related Sales Order(s)'
    )

    @api.multi
    @api.depends('invoice_line_ids')
    def _compute_sale_ids(self):
        for invoice in self:
            sale_ids = []
            for invoice_line in invoice.invoice_line_ids:
                if invoice_line.purchase_id:
                    sale_ids += invoice_line.purchase_id.sale_ids.ids
            if sale_ids:
                invoice.sale_ids = self.env["sale.order"].browse(sale_ids)
