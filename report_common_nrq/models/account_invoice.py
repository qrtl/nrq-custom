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

    #@api.onchange('origin')
    #def onchange_reference(self):
    #    for invoice in self:
    #        if invoice.origin:
    #            purchase_order = self.env['purchase.order'].search([('name', '=', invoice.origin)])
    #            if purchase_order:
    #                invoice.doc_title = purchase_order.doc_title
    #               invoice.reference =  purchase_order.partner_ref


    @api.onchange('invoice_line_ids')
    def _onchange_origin(self):
        res = super(ResPartner, self)._onchange_origin()
        purchase_ids = self.invoice_line_ids.mapped('purchase_id')
        self.doc_title = ""
        if purchase_ids:
            for title in purchase_ids.mapped('doc_title'):
                if title != False:
                    if self.doc_title == "":
                        self.doc_title += title
                    else:
                        self.doc_title += ", " + title