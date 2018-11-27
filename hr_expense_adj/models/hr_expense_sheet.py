# -*- coding: utf-8 -*-
# Copyright 2017-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'

    def _default_name(self):
        today = fields.Date.context_today(self)
        y, m, d = today.split('-')
        return y + '.' + m

    name = fields.Char(
        default=_default_name,
    )
    # add 'draft' state, and change default to draft
    state = fields.Selection(
        [('draft', 'Draft'),
         ('submit', 'Submitted'),
         ('approve', 'Approved'),
         ('post', 'Posted'),
         ('done', 'Paid'),
         ('cancel', 'Refused')],
        default='draft',
    )
    # add 'draft' state to cancel readonly for following fields
    employee_id = fields.Many2one(
        states={'draft': [('readonly', False)],
                'submit': [('readonly', False)]}
    )
    responsible_id = fields.Many2one(
        states={'draft': [('readonly', False)],
                'submit': [('readonly', False)]}
    )
    company_id = fields.Many2one(
        states={'draft': [('readonly', False)],
                'submit': [('readonly', False)]}
    )
    currency_id = fields.Many2one(
        states={'draft': [('readonly', False)],
                'submit': [('readonly', False)]}
    )
    # Overwrite default field definition
    expense_line_ids = fields.One2many('hr.expense', 'sheet_id',
                                       string='Expense Lines',
                                       states={'done': [('readonly', True)],
                                               'post': [('readonly', True)]},
                                       copy=False)

    def _assign_number(self, line):
        context = {'ir_sequence_date': line.date}
        line.number = self.env['ir.sequence'].with_context(context). \
            next_by_code('hr.expense')

    @api.model
    def create(self, vals):
        sheet = super(HrExpenseSheet, self).create(vals)
        for line in sheet.expense_line_ids.sorted(
                key=lambda x: (x.date, x.id)):
            self._assign_number(line)
        return sheet

    @api.multi
    def write(self, vals):
        res = super(HrExpenseSheet, self).write(vals)
        if self.state == 'submit':
            for line in self.expense_line_ids.sorted(
                    key=lambda x: (x.date, x.id)):
                if line.number == False:
                    self._assign_number(line)
            return res

    @api.multi
    def unlink(self):
        for line in self.expense_line_ids:
            line.number = False
        super(HrExpenseSheet, self).unlink()

    @api.multi
    def action_submit(self):
        return self.write({'state': 'submit'})

    @api.multi
    def action_cancel_submission(self):
        return self.write({'state': 'draft'})

    @api.multi
    def reset_expense_sheets(self):
        # override the standard method
        # return self.write({'state': 'submit'})
        return self.write({'state': 'draft'})
