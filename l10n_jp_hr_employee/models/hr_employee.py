# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import jaconv

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    family_name = fields.Char(
        'Family Name',
    )
    given_name = fields.Char(
        'Given Name',
    )
    furi_family_name = fields.Char(
        'Family Name Furigana',
    )
    furi_given_name = fields.Char(
        'Given Name Furigana',
    )
    employment_type_id = fields.Many2one(
        'hr.employment.type',
        string='Employment Type',
    )
    private_info_count = fields.Integer(
        compute='_compute_private_info_count',
        string='Private Info'
    )
    private_info_visible = fields.Boolean(
        compute='_compute_private_info_visible',
        string='Private Information Visibility',
    )

    @api.onchange('family_name')
    def _onchange_family_name(self):
        if self.family_name:
            self.family_name = jaconv.h2z(
                self.family_name, ascii=True, digit=True)

    @api.onchange('given_name')
    def _onchange_given_name(self):
        if self.given_name:
            self.given_name = jaconv.h2z(
                self.given_name, ascii=True, digit=True)

    @api.onchange('furi_family_name')
    def _onchange_furi_family_name(self):
        self.furi_family_name = jaconv.z2h(
            jaconv.hira2kata(self.furi_family_name))

    @api.onchange('furi_given_name')
    def _onchange_furi_given_name(self):
        self.furi_given_name = jaconv.z2h(
            jaconv.hira2kata(self.furi_given_name))

    def _compute_private_info_count(self):
        private_info_data = self.env['hr.private.info'].sudo().with_context(
            active_test=False).read_group(
            [('employee_id', 'in', self.ids)],
            ['employee_id'], ['employee_id'])
        result = dict((data['employee_id'][0], data['employee_id_count'])
                      for data in private_info_data)
        for employee in self:
            employee.private_info_count = result.get(employee.id, 0)

    @api.multi
    def action_view_private_info(self):
        private_info = self.env['hr.private.info'].with_context(
            active_test=False).search([('employee_id', '=', self.id)])
        action = self.env.ref(
            'l10n_jp_hr_employee.act_hr_employee_2_hr_private_info').read()[0]
        if len(private_info) > 1:
            action['domain'] = [('id', 'in', private_info.ids)]
        elif len(private_info) in [0, 1]:
            action['views'] = [(self.env.ref(
                'l10n_jp_hr_employee.view_hr_private_info_form').id, 'form')]
            if len(private_info) == 1:
                action['res_id'] = private_info.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action

    @api.multi
    def _compute_private_info_visible(self):
        for employee in self:
            employee.private_info_visible = True \
                if employee.user_id == self.env.user or \
                   self.env.user.has_group(
                       'l10n_jp_hr_employee.group_employee_private_info_manage')\
                else False

