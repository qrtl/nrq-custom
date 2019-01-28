# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class HrExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'

    @api.multi
    def post_expense_sheets(self):
        sheets = self.browse(self._context.get('active_ids', [])).filtered(
            lambda r: r.state == "approve")
        posted_sheets_ids = []
        for sheet in sheets:
            res = sheet.action_sheet_move_create()
            if res:
                posted_sheets_ids.append(sheet.id)
        return {
            'type': 'ir.actions.act_window',
            'name': _('Posted Expense Sheet(s)'),
            'res_model': 'hr.expense.sheet',
            'view_mode': 'form',
            'view_mode': 'tree',
            'domain': [('id', 'in', posted_sheets_ids)],
            'target': 'current'
        }
