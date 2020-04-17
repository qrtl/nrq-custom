# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmploymentType(models.Model):
    _name = 'hr.employment.type'

    name = fields.Char(
        required=True,
    )
