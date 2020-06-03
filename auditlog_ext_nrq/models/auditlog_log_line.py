# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import pytz
from odoo import api, fields, models


class AuditlogLogLine(models.Model):
    _inherit = 'auditlog.log.line'

    @api.model
    def create(self, vals):
        if vals.get('new_value_text') or vals.get('old_value_text'):
            old_value_text, new_value_text = vals.get(
                'old_value_text'), vals.get('new_value_text')
            timezone = pytz.timezone('Japan')
            try:
                new_value_text = pytz.UTC.localize(
                    fields.Datetime.from_string(new_value_text))
                new_value_text =\
                    fields.Datetime.to_string(
                        new_value_text.replace(
                            tzinfo=pytz.timezone('UTC')).astimezone(timezone))
                vals.update({
                    'new_value_text': new_value_text
                })
            except Exception:
                pass
            try:
                old_value_text = pytz.UTC.localize(
                    fields.Datetime.from_string(old_value_text))
                old_value_text =\
                    fields.Datetime.to_string(
                        old_value_text.replace(
                            tzinfo=pytz.timezone('UTC')).astimezone(timezone))
                vals.update({
                    'old_value_text': old_value_text
                })
            except Exception:
                pass
        return super(AuditlogLogLine, self).create(vals)
