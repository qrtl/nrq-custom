# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api, fields, models


class AuditlogLogLine(models.Model):
    _inherit = 'auditlog.log.line'

    @api.model
    def create(self, vals):
        if vals.get('new_value_text') or vals.get('old_value_text'):
            old_value_text, new_value_text = vals.get(
                'old_value_text'), vals.get('new_value_text')
            tz = self.env['res.users'].sudo().browse(SUPERUSER_ID).tz or 'UTC'
            try:
                new_value_text = fields.Datetime.to_string(
                    fields.Datetime.context_timestamp(
                        self.with_context(tz=tz),
                        fields.Datetime.from_string(new_value_text)))
                vals.update({
                    'new_value_text': new_value_text
                })
            except Exception:
                pass
            try:
                old_value_text = fields.Datetime.to_string(
                    fields.Datetime.context_timestamp(
                        self.with_context(tz=tz),
                        fields.Datetime.from_string(old_value_text)))
                vals.update({
                    'old_value_text': old_value_text
                })
            except Exception:
                pass
        return super(AuditlogLogLine, self).create(vals)
