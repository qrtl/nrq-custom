# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    _order = "date desc, id desc"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type',
        required=True,
    )
    related_analytic_type = fields.Selection(
        related="analytic_type_id.analytic_type",
    )
    pj_id = fields.Many2one(
        'project.project',
        string='Related Project',
        compute='_compute_pj_id',
        inverse='_set_account_id',
    )
    parent_project_id = fields.Many2one(
        related='pj_id.parent_project_id',
        string='Parent Project',
        store=True,
        readonly=True,
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        compute='_compute_employee_id',
        store=True,
    )

    @api.multi
    @api.depends('account_id')
    def _compute_pj_id(self):
        for line in self:
            if line.account_id and line.account_id.project_ids:
                for project in line.account_id.project_ids:
                    line.pj_id = project.id

    @api.multi
    def _set_account_id(self):
        for line in self:
            line.account_id = line.pj_id.analytic_account_id.id

    @api.multi
    @api.depends('user_id')
    def _compute_employee_id(self):
        for line in self:
            emp_ids = self.env['hr.employee'].search(
                [('user_id', '=', self.user_id.id)])
            line.employee_id = emp_ids and emp_ids[0] or False

    @api.onchange('general_account_id')
    def _onchange_analytic_type_id(self):
        self.analytic_type_id = self.general_account_id.analytic_type_id

    @api.model
    def create(self, vals):
        if vals.get('general_account_id', False) and\
            vals['general_account_id'] and not\
                vals.get('analytic_type_id', False):
            account_obj = self.env['account.account']
            account = account_obj.browse(vals['general_account_id'])
            vals.update(analytic_type_id=account.analytic_type_id.id)
        # assumption: project_id is included only for timesheet entries
        if vals.get('project_id', False):
            analytic_type_id = self.env['analytic.type'].search([
                ('analytic_type', '=', 'labour')])[0].id
            vals.update(analytic_type_id=analytic_type_id)
        return super(AccountAnalyticLine, self).create(vals)
