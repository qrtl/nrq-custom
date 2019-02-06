# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AnalyticType(models.Model):
    _name = 'analytic.type'
    _order = 'sequence'

    name = fields.Char(
        string="Name",
        translate=True,
        required=True
    )
    type = fields.Selection(selection=[
        ('sales', 'Sales'),
        ('labour', 'Labour'),
        ('outsourcing', 'Outsourcing'),
        ('expenses', 'Expenses'),
        ('advances', 'Advances'),
        ('other', 'Other')],
        string='Analytic Type',
        required=True,
    )
    sequence = fields.Integer(
        default=10,
        required=True,
    )
