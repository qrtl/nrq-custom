# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrAttendanceReason(models.Model):
    _name = 'hr.attendance.reason'

    name = fields.Char('Reason', required=True)
    active = fields.Boolean('Active', default=True)
