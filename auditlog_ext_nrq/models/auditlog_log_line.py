# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api, fields, models


class AuditlogLogLine(models.Model):
    _inherit = 'auditlog.log.line'

    def convert_time_to_users_timezone(self, value, tz):
        try:
            value = fields.Datetime.to_string(
                fields.Datetime.context_timestamp(
                    self.with_context(tz=tz),
                    fields.Datetime.from_string(value)))
            return value
        except Exception:
            return value

    @api.model
    def create(self, vals):
        tz = self.env['res.users'].sudo().browse(SUPERUSER_ID).tz or 'UTC'
        if vals.get('old_value_text'):
            vals.update({'old_value_text': self.convert_time_to_users_timezone(
                vals.get('old_value_text'), tz)})
        if vals.get('new_value_text'):
            vals.update({'new_value_text': self.convert_time_to_users_timezone(
                vals.get('new_value_text'), tz)})
        return super(AuditlogLogLine, self).create(vals)
