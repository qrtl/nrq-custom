# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    name_furigana = fields.Char(
        'Name Furigana',
    )
    employment_type_id = fields.Many2one(
        'hr.employment.type',
        string='Employment Type',
    )
    # private_info_ids = fields.One2many(
    #     'hr.private.info',
    #     'employee_id',
    #     string='Private Info')
    # private_info_id = fields.Many2one(
    #     'hr.private.info',
    #     compute='_compute_private_info_id',
    #     string='Latest Private Info',
    # )
    private_info_count = fields.Integer(
        compute='_compute_private_info_count',
        string='Private Info'
    )

    # def _compute_private_info_id(self):
    #     for info in self:
    #         info.private_info_id = info.private_info_ids[:1].id

    def _compute_private_info_count(self):
        private_info_data = self.env['hr.private.info'].sudo().read_group(
            [('employee_id', 'in', self.ids)],
            ['employee_id'], ['employee_id'])
        result = dict((data['employee_id'][0], data['employee_id_count'])
                      for data in private_info_data)
        for employee in self:
            employee.private_info_count = result.get(employee.id, 0)
