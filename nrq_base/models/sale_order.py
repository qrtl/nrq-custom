# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    doc_title = fields.Char(
        string="Doc Title",
    )

    @api.multi
    def _prepare_invoice(self):
        result = super(SaleOrder, self)._prepare_invoice()
        result.update({'doc_title': self.doc_title})
        return result