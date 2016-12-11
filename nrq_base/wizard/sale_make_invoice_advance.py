# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        invoice =\
            super(SaleAdvancePaymentInv, self)._create_invoice(order,
                                                               so_line,
                                                               amount)
        if invoice:
            invoice.doc_title = order.doc_title
        return invoice
