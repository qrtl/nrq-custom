# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrDisabilityClass(models.Model):
    _name = 'hr.disability.class'

    name = fields.Char(
        required=True,
    )
