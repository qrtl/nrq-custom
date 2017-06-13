# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'account.invoice'

    delivery_note = fields.Boolean(
        string="Delivery Note",
    )
    doc_title = fields.Char(
        string="Doc Title",
    )

    @api.onchange('partner_id')
    def onchange_partner(self):
        for invoice in self:
            invoice.delivery_note = invoice.partner_id.delivery_note

    @api.onchange('invoice_line_ids')
    def _onchange_origin(self):
        purchase_ids = self.invoice_line_ids.mapped('purchase_id')
        if purchase_ids:
            self.origin = ', '.join(purchase_ids.mapped('name'))
            self.doc_title = ""
            for title in purchase_ids.mapped('doc_title'):
                if title != False:
                    if self.doc_title == "":
                        self.doc_title += title
                    else:
                        self.doc_title += ", " + title
