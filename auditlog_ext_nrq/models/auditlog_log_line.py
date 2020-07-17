# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api, fields, models


class AuditlogLogLine(models.Model):
    _inherit = 'auditlog.log.line'

    @api.model
    def create(self, vals):
        tz = self.env['res.users'].sudo().browse(SUPERUSER_ID).tz or 'UTC'
        for field in ["old_value_text", "new_value_text"]:
            val = vals.get(field)
            if val:
                try:
                    converted_time = fields.Datetime.to_string(
                        fields.Datetime.context_timestamp(
                            self.with_context(tz=tz),
                            fields.Datetime.from_string(val)))
                    vals.update({field: converted_time})
                except Exception:
                    pass
        return super(AuditlogLogLine, self).create(vals)
