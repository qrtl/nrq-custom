# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    delivery_note = fields.Boolean(
        string="Delivery Note",
        help="Select if delivery note should be printed together with "
             "invoice.",
    )
