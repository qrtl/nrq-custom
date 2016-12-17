# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    show_tax = fields.Boolean(
        string="Show Tax",
        help="Show tax in printed quotation."
    )
    doc_title = fields.Char(
        string="Doc Title",
    )


    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({'doc_title': self.doc_title})
        return res
