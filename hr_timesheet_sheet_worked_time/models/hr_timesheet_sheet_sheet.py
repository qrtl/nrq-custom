# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from odoo import models, fields, api


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
        store=False
    )

    @api.depends('standard_work_hours')
    def _compute_expected_work_hours(self):
        for sheet in self:
            public_holidays = self.env['hr.holidays.public'].search(
                [('year', '=', datetime.now().year),
                 ('country_id', '=', self.user_id.partner_id.country_id.id)]
            )
            holiday_hours = 0.0
            for line in public_holidays.mapped('line_ids'):
                public_holiday = \
                    sheet.employee_id.calendar_id.attendance_ids.filtered(
                        lambda x: x.date_from == line.date or
                        x.date_to == line.date)
                if public_holiday:
                    for attendance in public_holiday:
                        holiday_hours += \
                            attendance.hour_from - attendance.hour_to
            sheet.expected_work_hours = \
                self.standard_work_hours - abs(holiday_hours)

    @api.depends('expected_work_hours', 'total_timesheet')
    def _compute_overtime_hours(self):
        self.overtime_hours = self.total_timesheet - self.expected_work_hours

    @api.depends(
        'employee_id.calendar_id',
        'employee_id.calendar_id.attendance_ids'
    )
    def _compute_standard_work_hours(self):
        for sheet in self:
            if sheet.employee_id and sheet.employee_id.calendar_id:
                total_time = 0.0
                attendance_ids = \
                    sheet.employee_id.calendar_id.attendance_ids.filtered(
                        lambda x: (
                            (x.date_from <= self.date_to and
                             x.date_to >= self.date_from)))
                for attendance in attendance_ids:
                    total_time += attendance.hour_from - attendance.hour_to
                sheet.standard_work_hours = abs(total_time)
