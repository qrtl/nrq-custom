# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrQualification(models.Model):

    _inherit = "hr.qualification"

    parent_id = fields.Many2one(related="employee_id.parent_id")
    department_id = fields.Many2one(related="employee_id.department_id")
    active = fields.Boolean(related="employee_id.active")
