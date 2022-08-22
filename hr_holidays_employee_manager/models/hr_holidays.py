# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HrHolidays(models.Model):
    _inherit = "hr.holidays"

    employee_manager_id = fields.Many2one(
        related="employee_id.parent_id",
        string="Employee Manager",
        readonly=True,
        store=True,
        help="Manager of the employee according to the employee settings",
    )
