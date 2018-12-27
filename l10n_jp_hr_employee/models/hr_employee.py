# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    furigana = fields.Char(
        required=True,
    )
    employment_type_id = fields.Many2one(
        'hr.employment.type',
        string='Employment Type',
    )
    # private_info_id = fields.Many2one(
    #     'hr.private.info', 'Product Template',
    #     auto_join=True, index=True, ondelete="cascade", required=True)
    private_info_ids = fields.One2many(
        'hr.private.info',
        'employee_id',
        string='Private Info')
    # private_info_id = fields.Many2one(
    #     'hr.private.info',
    #     compute='_compute_private_info_id',
    #     string='Latest Private Info',
    # )
    #
    # def _compute_private_info_id(self):
    #     PrivateInfo = self.env['hr.private.info']
    #     for employee in self:
    #         employee.private_info_id = PrivateInfo.search([('employee_id', '=', employee.id)], order='date_start desc', limit=1)
