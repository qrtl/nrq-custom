# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime, timedelta

from odoo import api, fields, models
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
    timesheet_expected_work_hours = fields.Float(
        compute='_compute_timesheet_expected_work_hours',
        string="Timesheet Expected Working Hours",
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
            sheet.holiday_hours = sheet.get_holiday_hours(
                fields.Datetime.to_string(datetime.now().date()))

    @api.multi
    def _compute_expected_work_hours(self):
        for sheet in self:
            sheet.expected_work_hours = sheet.standard_work_hours - \
                sheet.holiday_hours

    @api.multi
    def _compute_timesheet_expected_work_hours(self):
        for sheet in self:
            sheet.timesheet_expected_work_hours = \
                sheet.get_standard_work_hours(sheet.date_to) - \
                sheet.get_holiday_hours(sheet.date_to)

    @api.multi
    def _compute_overtime_hours(self):
        for sheet in self:
            sheet.overtime_hours = sheet.total_timesheet - \
                sheet.expected_work_hours

    @api.multi
    def _compute_standard_work_hours(self):
        for sheet in self:
            sheet.standard_work_hours = sheet.get_standard_work_hours(
                datetime.now().date())

    def get_holiday_hours(self, date):
        date_to = date if self.date_to > date else self.date_to
        public_holiday_line_ids = self.env['hr.holidays.public.line'].search([
            ('date', '>=', self.date_from),
            ('date', '<=', date_to),
        ])
        holiday_hours = 0.0
        for line in public_holiday_line_ids:
            public_holiday = datetime.strptime(
                str(line.date), DEFAULT_SERVER_DATE_FORMAT)
            attendance_ids = self.employee_id.calendar_id.attendance_ids.\
                filtered(
                    lambda attendance: int(attendance.dayofweek) ==
                    public_holiday.weekday())
            for attendance in attendance_ids:
                holiday_hours += \
                    attendance.hour_to - attendance.hour_from
        return holiday_hours

    def get_standard_work_hours(self, date):
        date = datetime.strptime(str(date), DEFAULT_SERVER_DATE_FORMAT).date()
        date_from = datetime.strptime(str(
            self.date_from), DEFAULT_SERVER_DATE_FORMAT).date()
        date_to = datetime.strptime(str(
            self.date_to), DEFAULT_SERVER_DATE_FORMAT).date()
        day_count = (date_to - date_from).days if date_to < date else (
            date - date_from).days
        total_time = 0.0
        for single_date in (
                date_from + timedelta(n)
                for n in range(day_count + 1)):
            attendance_ids = \
                self.employee_id.calendar_id.attendance_ids.filtered(
                    lambda attendance: int(
                        attendance.dayofweek) == single_date.weekday())
            for attendance in attendance_ids:
                total_time += attendance.hour_to - attendance.hour_from
        return total_time
