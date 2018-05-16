# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    update_manually = fields.Boolean(
        string='Updated Manually',
        default=False,
    )
    state = fields.Selection(
        related='sheet_id.state',
        readonly=True,
    )

    @api.onchange('employee_id', 'check_in', 'check_out')
    def _onchange_update_manually(self):
        self.update_manually = True
