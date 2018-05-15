# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    worked_hours = fields.Char(
        string='Worked Hours',
        compute='_compute_worked_hours',
        readonly=True,
    )
    adjust_attendance_reason_id = fields.Many2one(
        'hr.attendance.reason',
        string='Reason of Adjustment',
    )
    update_manually = fields.Boolean(
        string='Updated Manually',
        default=False,
    )
    state = fields.Selection(
        related='sheet_id.state',
        readonly=True,
    )

    @api.multi
    @api.depends('check_in', 'check_out')
    def _compute_worked_hours(self):
        for attendance in self:
            if attendance.check_in and attendance.check_out:
                diff = fields.Datetime.from_string(attendance.check_out) - \
                       fields.Datetime.from_string(attendance.check_in)
                attendance.worked_hours = str(diff)

    @api.onchange('employee_id', 'check_in', 'check_out',
                  'adjust_attendance_reason_id')
    def _onchange_update_manually(self):
        self.update_manually = True
