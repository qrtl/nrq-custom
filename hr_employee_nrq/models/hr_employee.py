# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from dateutil.relativedelta import relativedelta
from odoo import _, api, fields, models
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _order = 'code, name'

    date_of_joining = fields.Date(
        'Date of Joining'
    )
    year_enrolled = fields.Char(
        compute='_get_year_enrolled'
    )
    employee_info_visible = fields.Boolean(
        compute='_compute_employee_info_visible',
        string='Employee Information Visibility',
    )

    @api.multi
    def _get_year_enrolled(self):
        for employee in self:
            if employee.date_of_joining:
                date_of_joining = datetime.strptime(
                    employee.date_of_joining, DEFAULT_SERVER_DATE_FORMAT)
                today = datetime.strptime(fields.Date.context_today(self),
                                          DEFAULT_SERVER_DATE_FORMAT)
                difference = relativedelta(today, date_of_joining)
                employee.year_enrolled = _("%s Year %s Month(s)") % (
                    difference.years or '0', difference.months or '0'
                )

    @api.multi
    def _compute_employee_info_visible(self):
        for employee in self:
            employee.employee_info_visible = True \
                if employee.user_id == self.env.user or \
                   self.env.user.has_group('hr.group_hr_user') else False
