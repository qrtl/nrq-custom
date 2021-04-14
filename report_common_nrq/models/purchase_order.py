# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    doc_title = fields.Char(string="Doc Title",)
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Salesperson",
        track_visibility="onchange",
        default=lambda self: self.env.user,
    )
