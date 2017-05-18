# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    name = fields.Char(
        string='Expense Description',
        help="""
        Please describe the usage of the expense.
        Examples:
        For transporation expenses:
        - Train (Shibuya - Ichigaya)
        - Bus (Shibuya - Ichigaya)
        - Commuter pass (6-month, Shibuya - Ichigaya)
        - Taxi (Shibuya - Ichigaya)
        For meeting expenses:
        - Food and drinks - 2 from NQ, 1 from XXX
        For entertainment expenses:
        - Food and drinks - 2 from NQ, 1 from XXX
        """
    )
    number = fields.Char(
        readonly=True,
        copy=False,
    )
    reference = fields.Char(
        help="""
        Please put the approval number (NOT the document number) here.
        Reference should be provided for expenses of purchasing goods, entertainment or business trip.
        """
    )

    @api.multi
    def submit_expenses(self):
        date = max(line.date for line in self)
        y, m, d = date.split('-')
        res = super(HrExpense, self).submit_expenses()
        res['context']['default_name'] = y + '.' + m
        return res

    @api.multi
    def write(self, vals):
        if 'sheet_id' in vals and not vals.get('sheet_id'):
            vals['number'] = False
        return super(HrExpense, self).write(vals)
