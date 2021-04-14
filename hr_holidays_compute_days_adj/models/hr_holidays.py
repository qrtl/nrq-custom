# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrHolidays(models.Model):
    _inherit = "hr.holidays"

    from_full_day = fields.Boolean(default=True)
    to_full_day = fields.Boolean(default=True)
    # Set default to avoid null value if user does not create the leave record
    # from calendar value
    date_from = fields.Datetime(default=fields.Datetime.now)
    date_to = fields.Datetime(default=fields.Datetime.now)
