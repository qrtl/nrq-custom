# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    move_partner_id = fields.Many2one(
        related='move_id.partner_id',
        string='Move Line Partner',
        readonly=True,
        store=True,
    )
