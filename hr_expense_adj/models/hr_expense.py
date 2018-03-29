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
        Reference should be provided for expenses of purchasing goods,
        entertainment or business trip.
        """
    )
    # just to assign a compute method as hiding account_id in view nullifies
    # the effect of standard _onchange_product_id method
    account_id = fields.Many2one(
        compute='_compute_account_id',
        store=True,
    )

    # override the standard method
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            # QTL: prevent updates of name and unit_amount
            # if not self.name:
            #     self.name = self.product_id.display_name or ''
            # self.unit_amount = self.product_id.price_compute(
            # 'standard_price')[self.product_id.id]
            self.product_uom_id = self.product_id.uom_id
            self.tax_ids = self.product_id.supplier_taxes_id
            account = self.product_id.product_tmpl_id._get_product_accounts()[
                'expense']
            if account:
                self.account_id = account

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

    @api.multi
    @api.depends('product_id')
    def _compute_account_id(self):
        for exp in self:
            account = exp.product_id.product_tmpl_id._get_product_accounts()[
                'expense']
            if account:
                exp.account_id = account
