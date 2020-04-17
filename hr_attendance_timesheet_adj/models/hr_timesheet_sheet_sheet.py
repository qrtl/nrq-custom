# -*- coding: utf-8 -*-
# Copyright 2018-2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class HrTimesheetSheet(models.Model):
    _inherit = 'hr_timesheet_sheet.sheet'

    total_attendances_worked_hours = fields.Float(
        compute='_compute_total_attendances_worked_hours',
        string="Total Attendances Worked Hours",
    )
    code = fields.Char(
        related='employee_id.code',
        string='Code',
        store=True,
        readonly=True,
    )

    @api.multi
    @api.depends('attendances_ids')
    def _compute_total_attendances_worked_hours(self):
        for sheet in self:
            worked_hours = 0.0
            for attendance in sheet.attendances_ids:
                worked_hours += attendance.worked_hours
            sheet.total_attendances_worked_hours = worked_hours

    @api.multi
    def action_attendance_list(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Attendances'),
            'res_model': 'hr.attendance',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'context': {
                'search_default_sheet_id': self.id
            }
        }
