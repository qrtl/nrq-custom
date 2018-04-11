# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    analytic_type_id = fields.Many2one(
        'analytic.type',
        string='Analytic Type'
    )
