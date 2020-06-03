# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class HrTimesheetSheet(models.Model):
    _inherit = 'hr_timesheet_sheet.sheet'

    standard_work_hours = fields.Float(
        compute='_compute_standard_work_hours',
        string="Standard Working Hours",
    )
    expected_work_hours = fields.Float(
        compute='_compute_expected_work_hours',
        string="Expected Working Hours",
    )
    overtime_hours = fields.Float(
        compute='_compute_overtime_hours',
        string="Overtime Working Hours",
    )
    holiday_hours = fields.Float(
        compute='_compute_holiday_hours',
        string="Holiday Hours",
    )

    @api.multi
    def _compute_holiday_hours(self):
        for sheet in self:
            today_date = fields.Datetime.to_string(datetime.now().date())
            date_to = sheet.date_to
            if sheet.date_to > today_date:
                date_to = today_date
            public_holiday_line_ids = self.env[
                'hr.holidays.public.line'].search(
                [
                    ('date', '>=', sheet.date_from),
                    ('date', '<=', date_to),
                    ('year_id.year', '=', datetime.now().year),
                ])
            holiday_hours = 0.0
            for line in public_holiday_line_ids:
                public_holiday = datetime.strptime(
                    str(line.date), DEFAULT_SERVER_DATE_FORMAT)
                attendance_ids = sheet.employee_id.calendar_id.attendance_ids.filtered(
                    lambda attendance: int(
                        attendance.dayofweek) == public_holiday.weekday())
                for attendance in attendance_ids:
                    holiday_hours += \
                        attendance.hour_to - attendance.hour_from
            sheet.holiday_hours = holiday_hours

    @api.multi
    def _compute_expected_work_hours(self):
        for sheet in self:
            sheet.expected_work_hours = sheet.standard_work_hours - sheet.holiday_hours

    @api.multi
    def _compute_overtime_hours(self):
        for sheet in self:
            sheet.overtime_hours = sheet.total_timesheet - sheet.expected_work_hours

    @api.multi
    def _compute_standard_work_hours(self):
        for sheet in self:
            today_date = fields.Datetime.to_string(datetime.now().date())
            date_from = datetime.strptime(str(
                sheet.date_from), DEFAULT_SERVER_DATE_FORMAT).date()
            date_to = datetime.strptime(str(
                sheet.date_to), DEFAULT_SERVER_DATE_FORMAT).date()
            day_count = (datetime.now().date() - date_from).days
            if sheet.date_to < today_date:
                day_count = (date_to - date_from).days
            total_time = 0.0
            for single_date in (
                    date_from + timedelta(n)
                    for n in range(day_count + 1)):
                attendance_ids = \
                    sheet.employee_id.calendar_id.attendance_ids.filtered(
                        lambda attendance: int(
                            attendance.dayofweek) == single_date.weekday())
                for attendance in attendance_ids:
                    total_time += attendance.hour_to - attendance.hour_from
            sheet.standard_work_hours = total_time
