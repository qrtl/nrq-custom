# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    # we cannot make this field required at model level because that would
    # interfere the record creation from HrTimesheetSheet thru JS
    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type',
        # required=True,
    )
    related_analytic_type = fields.Selection(
        related="analytic_type_id.type",
        readonly=True,
    )
    pj_id = fields.Many2one(
        'project.project',
        string='Related Project',
        compute='_compute_pj_id',
        inverse='_set_account_id',
        store=True,
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
        readonly=True,
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Department',
        compute='_compute_employee_id',
        store=True,
        readonly=True,
    )
    sale_id = fields.Many2one(
        'sale.order',
        string='Sales Order',
        compute='_compute_pj_id',
        store=True,
        readonly=True,
    )
    purchase_id = fields.Many2one(
        'purchase.order',
        string='Purchase Order',
        readonly=True,
    )
    team_id = fields.Many2one(
        related='sale_id.team_id',
        store=True,
        readonly=True,
    )
    sale_user_id = fields.Many2one(
        related='sale_id.user_id',
        store=True,
        readonly=True,
    )
    sale_employee_id = fields.Many2one(
        'hr.employee',
        string='Salesperson',
        compute='_compute_sale_employee_id',
        store=True,
        readonly=True,
    )
    # to be used in pivot view
    amount_int = fields.Integer(
        'Amount',
        compute='_compute_amount_int',
        store=True,
        readonly=True,
    )

    @api.multi
    @api.depends('account_id')
    def _compute_pj_id(self):
        for ln in self:
            projects = ln.account_id and ln.account_id.project_ids
            ln.pj_id = projects and projects[0].id or False
            sale_orders = self.env['sale.order'].search(
                [('project_id', '=', ln.account_id.id),
                 ('state', '!=', 'cancel')])
            if len(sale_orders) == 1 and sale_orders[0].project_project_id:
                ln.sale_id = sale_orders[0].id

    @api.multi
    def _set_account_id(self):
        for line in self:
            line.account_id = line.pj_id.analytic_account_id.id

    @api.multi
    @api.depends('user_id')
    def _compute_employee_id(self):
        for line in self:
            emp_ids = self.env['hr.employee'].search(
                [('user_id', '=', line.user_id.id)])
            if emp_ids:
                line.employee_id = emp_ids[0]
                line.department_id = emp_ids[0].department_id

    @api.multi
    @api.depends('sale_user_id')
    def _compute_sale_employee_id(self):
        for line in self:
            if line.sale_user_id:
                emp_ids = self.env['hr.employee'].search(
                    [('user_id', '=', line.sale_user_id.id)])
                if emp_ids:
                    line.sale_employee_id = emp_ids[0]

    @api.multi
    @api.depends('amount')
    def _compute_amount_int(self):
        for line in self:
            line.amount_int = int(line.amount)

    @api.onchange('general_account_id')
    def _onchange_analytic_type_id(self):
        self.analytic_type_id = self.general_account_id.analytic_type_id

    @api.model
    def create(self, vals):
        analytic_type = False
        purchase_id = False
        if vals.get('general_account_id') and not vals.get('analytic_type_id'):
            account = self.env['account.account'].browse(
                vals['general_account_id'])
            analytic_type = account.analytic_type_id
        # assumption: project_id is included only for timesheet entries
        if vals.get('project_id'):
            analytic_type = self.env['analytic.type'].sudo().search([
                ('type', '=', 'labour')])[0]
        if analytic_type and analytic_type.type not in ['sales', 'labour']:
            move_line_id = vals.get('move_id')
            if move_line_id:
                move_line = self.env['account.move.line'].browse(move_line_id)
                invoice = move_line.invoice_id
                if invoice and invoice.type in ['in_invoice', 'in_refund']:
                    invoice_lines = invoice.invoice_line_ids.filtered(
                        lambda r: r.account_analytic_id.id == vals[
                            'account_id'])
                    purchase_line = invoice_lines[0].mapped(
                        'purchase_line_id') if invoice_lines else False
                    if purchase_line:
                        purchase_id = self.env['purchase.order.line'].browse(
                            purchase_line.id).order_id.id
        vals['analytic_type_id'] = analytic_type and analytic_type.id or False
        vals['purchase_id'] = purchase_id
        return super(AccountAnalyticLine, self).create(vals)
