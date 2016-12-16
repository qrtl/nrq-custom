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
