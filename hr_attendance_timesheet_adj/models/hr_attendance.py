# -*- coding: utf-8 -*-
# Copyright 2018-2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from pytz import timezone
import pytz

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    update_manually = fields.Boolean(
        string='Updated Manually',
        default=False,
    )
    update_manually_reason = fields.Char(
        string='Updated Manually Reason',
    )
    state = fields.Selection(
        related='sheet_id.state',
        readonly=True,
    )

    @api.constrains('update_manually', 'update_manually_reason')
    def _check_update_manually(self):
        if self.update_manually and not self.update_manually_reason:
            raise ValidationError(
                _('Please enter the reason of updating the attendance record.'))

    @api.onchange('employee_id', 'check_in', 'check_out')
    def _onchange_update_manually(self):
        self.update_manually = True

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
                ts.date_from, DEFAULT_SERVER_DATE_FORMAT)).replace(
                    hour=0, minute=0, second=0)
            local_date_to_dt = local_tz.localize(datetime.strptime(
                ts.date_to, DEFAULT_SERVER_DATE_FORMAT)).replace(
                    hour=23, minute=59, second=59)
            utc_date_from_dt = local_date_from_dt.astimezone(
                pytz.utc).strftime('%Y-%m-%d %H:%M:%S')
            utc_date_to_dt = local_date_to_dt.astimezone(pytz.utc).strftime(
                '%Y-%m-%d %H:%M:%S')
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
