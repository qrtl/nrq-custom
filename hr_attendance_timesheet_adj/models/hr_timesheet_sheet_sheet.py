# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
from odoo.tools.translate import _


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

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
