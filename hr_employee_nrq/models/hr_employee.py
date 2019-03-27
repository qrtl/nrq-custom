# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from dateutil.relativedelta import relativedelta
from datetime import datetime


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _order = 'code, name'

    date_of_joining = fields.Date(
        'Date of Joining'
    )
    year_enrolled = fields.Char(
        compute='_get_year_enrolled'
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
