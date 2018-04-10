# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type'
    )
