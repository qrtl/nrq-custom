# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from pytz import timezone
import pytz

from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.addons.hr_timesheet_attendance.models.hr_attendance import HrAttendance

# Monkey Patching
# Overwrite the original _compute_sheet and _search_sheet in hr_timesheet_attendance
@api.depends('employee_id', 'check_in', 'check_out',
                 'sheet_id_computed.date_to',
                 'sheet_id_computed.date_from',
                 'sheet_id_computed.employee_id')
def _compute_sheet(self):
    """Links the attendance to the corresponding sheet
    """
    for attendance in self:
        att_tz_date_str = attendance._get_attendance_employee_tz(
            attendance.employee_id.id, attendance.check_in)
        corresponding_sheet = self.env[
            'hr_timesheet_sheet.sheet'].search(
            [('date_to', '>=', att_tz_date_str),
             ('date_from', '<=', att_tz_date_str),
             ('employee_id', '=', attendance.employee_id.id),
             ('state', 'in', ['draft', 'new'])], limit=1)
        if corresponding_sheet:
            attendance.sheet_id_computed = corresponding_sheet[0]
            attendance.sheet_id = corresponding_sheet[0]

def _search_sheet(self, operator, value):
    assert operator == 'in'
    ids = []
    for ts in self.env['hr_timesheet_sheet.sheet'].browse(value):
        local_tz = timezone(
            ts.employee_id.user_id.partner_id.tz or 'utc')
        local_date_from_dt = local_tz.localize(datetime.strptime(
            ts.date_from, DEFAULT_SERVER_DATE_FORMAT))
        local_date_to_dt = local_tz.localize(datetime.strptime(
            ts.date_to, DEFAULT_SERVER_DATE_FORMAT))
        utc_date_from_dt = local_date_from_dt.astimezone(pytz.utc)
        utc_date_to_dt = local_date_to_dt.astimezone(pytz.utc)
        self._cr.execute("""
                SELECT a.id
                    FROM hr_attendance a
                WHERE %(date_to)s >= a.check_in
                    AND %(date_from)s <= a.check_in
                    AND %(employee_id)s = a.employee_id
                GROUP BY a.id""", {'date_from': utc_date_from_dt,
                                   'date_to': utc_date_to_dt,
                                   'employee_id': ts.employee_id.id, })
        ids.extend([row[0] for row in self._cr.fetchall()])
    return [('id', 'in', ids)]

class HrAttendanceHookComputeSheet(models.AbstractModel):
    _name = "hr.attendance.hook.compute.sheet"
    _description = "Provide hook point for _compute_sheet method"

    def _register_hook(self):
        HrAttendance._compute_sheet = _compute_sheet
        return super(HrAttendanceHookComputeSheet, self)._register_hook()

class HrAttendanceHookSearchSheet(models.AbstractModel):
    _name = "hr.attendance.hook.search.sheet"
    _description = "Provide hook point for _search_sheet method"

    def _register_hook(self):
        HrAttendance._search_sheet = _search_sheet
        return super(HrAttendanceHookSearchSheet, self)._register_hook()
