# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class HrTimesheetSheet(models.Model):
    _inherit = 'hr_timesheet_sheet.sheet'

    standard_work_hours = fields.Float(
        compute='_compute_standard_work_hours',
        string="Standard Work Hours",
    )
    expected_work_hours = fields.Float(
        compute='_compute_expected_work_hours',
        string="Expected Work Hours",
    )
    overtime_hours = fields.Float(
        compute='_compute_overtime_hours',
        string="Overtime Hours",
    )
    holiday_hours = fields.Float(
        compute='_compute_holiday_hours',
        string="Holiday Hours",
    )

    @api.depends(
        'employee_id.calendar_id',
        'employee_id.calendar_id.attendance_ids',
        'employee_id.calendar_id.attendance_ids.dayofweek'
    )
    def _compute_holiday_hours(self):
        for sheet in self:
            public_holidays = self.env['hr.holidays.public.line'].search(
                [
                    ('date', '>=', sheet.date_from),
                    ('date', '<=', sheet.date_to),
                    ('year_id.year', '=', datetime.now().year),
                    ('year_id.country_id', '=',
                     self.user_id.partner_id.country_id.id)
                ]
            )
            holiday_hours = 0.0
            for line in public_holidays:
                public_holiday = datetime.strptime(str(line.date),
                                                   DEFAULT_SERVER_DATE_FORMAT)
                attendance_ids = sheet.employee_id.calendar_id.attendance_ids.filtered(
                    lambda attendance: int(
                        attendance.dayofweek) == public_holiday.weekday())
                for attendance in attendance_ids:
                    holiday_hours += \
                        attendance.hour_from - attendance.hour_to
            sheet.holiday_hours = abs(holiday_hours)

    @api.depends('standard_work_hours', 'holiday_hours')
    def _compute_expected_work_hours(self):
        self.expected_work_hours = self.standard_work_hours - self.holiday_hours

    @api.depends('expected_work_hours', 'total_timesheet')
    def _compute_overtime_hours(self):
        self.overtime_hours = self.total_timesheet - self.expected_work_hours

    @api.depends(
        'employee_id.calendar_id',
        'employee_id.calendar_id.attendance_ids',
        'employee_id.calendar_id.attendance_ids.dayofweek'
    )
    def _compute_standard_work_hours(self):
        for sheet in self:
            start_date = datetime.strptime(str(
                self.date_from), DEFAULT_SERVER_DATE_FORMAT)
            end_date = datetime.strptime(str(
                self.date_to), DEFAULT_SERVER_DATE_FORMAT)
            attendance_ids = sheet.employee_id.calendar_id.attendance_ids.filtered(
                lambda attendance: int(
                    attendance.dayofweek) in range(start_date.weekday(),
                                                   end_date.weekday()))
            total_time = 0.0
            for attendance in attendance_ids:
                total_time += attendance.hour_from - attendance.hour_to
            sheet.standard_work_hours = abs(total_time)
