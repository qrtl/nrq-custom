# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrPrivateInfo(models.Model):
    _name = 'hr.private.info'

    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
    )
    private_country_id = fields.Many2one(
        'res.country',
        string='Nationality (Private)',
    )
