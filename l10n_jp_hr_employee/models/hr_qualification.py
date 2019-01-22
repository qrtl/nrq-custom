# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api

from datetime import datetime


def get_years():
    year_list = []
    for i in range(1960, datetime.today().year + 1):
        year_list.append((i, str(i)))
    return year_list


class HrQualification(models.Model):
    _name = 'hr.qualification'
    _order = 'year, month'

    name = fields.Char(
        required=True,
    )
    private_info_id = fields.Many2one(
        'hr.private.info',
        string='Private Info',
    )
    employee_id = fields.Many2one(
        related='private_info_id.employee_id',
        store=True,
    )
    year = fields.Selection(
        get_years(),
    )
    month = fields.Selection(
        [('1', 'January'),
         ('2', 'February'),
         ('3', 'March'),
         ('4', 'April'),
         ('5', 'May'),
         ('6', 'June'),
         ('7', 'July'),
         ('8', 'August'),
         ('9', 'September'),
         ('10', 'October'),
         ('11', 'November'),
         ('12', 'December')]
    )
    date_expiry = fields.Date(
        "Expiry Date",
    )
    reference = fields.Char()
