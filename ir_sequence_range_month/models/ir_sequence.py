# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import calendar
from datetime import datetime, timedelta

from odoo import fields, models


class IrSequence(models.Model):
    _inherit = "ir.sequence"

    def _get_month_date_range(self, date, year):
        month = fields.Date.from_string(date).strftime("%m")
        _, num_days = calendar.monthrange(int(year), int(month.replace("0", "")))
        date_from = "{}-{}-01".format(year, month)
        date_to = "{}-{}-{}".format(year, month, num_days)
        return date_from, date_to

    # override the standard method to handle the case where numbers should be
    # refreshed monthly
    def _create_date_range_seq(self, date):
        year = fields.Date.from_string(date).strftime("%Y")
        date_from = "{}-01-01".format(year)
        date_to = "{}-12-31".format(year)
        if "range_month" in self.prefix:  # qtl
            date_from, date_to = self._get_month_date_range(date, year)  # qtl
        date_range = self.env["ir.sequence.date_range"].search(
            [
                ("sequence_id", "=", self.id),
                ("date_from", ">=", date),
                ("date_from", "<=", date_to),
            ],
            order="date_from desc",
        )
        if date_range:
            date_to = datetime.strptime(date_range.date_from, "%Y-%m-%d") + timedelta(
                days=-1
            )
            date_to = date_to.strftime("%Y-%m-%d")
        date_range = self.env["ir.sequence.date_range"].search(
            [
                ("sequence_id", "=", self.id),
                ("date_to", ">=", date_from),
                ("date_to", "<=", date),
            ],
            order="date_to desc",
        )
        if date_range:
            date_from = datetime.strptime(date_range.date_to, "%Y-%m-%d") + timedelta(
                days=1
            )
            date_from = date_from.strftime("%Y-%m-%d")
        seq_date_range = (
            self.env["ir.sequence.date_range"]
            .sudo()
            .create(
                {"date_from": date_from, "date_to": date_to, "sequence_id": self.id}
            )
        )
        return seq_date_range
