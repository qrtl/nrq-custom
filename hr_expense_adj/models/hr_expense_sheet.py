# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class HrExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'

    def _default_name(self):
        today = fields.Date.context_today(self)
        y, m, d = today.split('-')
        return y + '.' + m

    name = fields.Char(
        default=_default_name,
    )
