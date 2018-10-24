# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice.line'

    sale_ids = fields.Many2many(
        'sale.order',
        compute="_compute_sale_ids",
        store=True,
        string='Related Sales Order(s)'
    )

    @api.multi
    @api.depends('account_analytic_id')
    def _compute_sale_ids(self):
        for invoice_line in self:
            if invoice_line.account_analytic_id and \
                    invoice_line.invoice_id.type in ('in_invoice',
                                                     'in_refund'):
                invoice_line.sale_ids = self.env["sale.order"].search([(
                    "project_id", "=", invoice_line.account_analytic_id.id)])
