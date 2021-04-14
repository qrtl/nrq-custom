# -*- coding: utf-8 -*-
# Copyright 2018-2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    project_manager_user_id = fields.Many2one(
        related="project_project_id.user_id", string="Project Manager",
    )
    gross_profit_margin_input = fields.Char(
        string="Gross Profit Margin", required=True,
    )
    gross_profit_margin = fields.Float(string="Gross Profit Margin",)

    @api.onchange("gross_profit_margin_input")
    def _onchange_gross_profit_margin_input(self):
        if self.gross_profit_margin_input:
            try:
                self.gross_profit_margin = float(self.gross_profit_margin_input)
            except Exception:
                raise UserError(_("The gross_profit_margin must be a number."))
