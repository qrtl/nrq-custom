# -*- coding: utf-8 -*-
# Copyright 2019-2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AuditlogLog(models.Model):
    _inherit = "auditlog.log"

    log_category = fields.Selection(
        [
            ("state_update", "Submitted/Set back to Draft"),
            ("fields_update", "Fields Update"),
            ("create", "Record Created"),
            ("unlink", "Record Unlinked"),
            ("other", "N/A"),
        ],
        string="Log Category",
        compute="_compute_log_category",
        store=True,
    )

    @api.multi
    @api.depends("line_ids")
    def _compute_log_category(self):
        for log in self:
            log.log_category = "other"
            if log.method == "write" and log.line_ids:
                log.log_category = (
                    "state_update"
                    if log.line_ids.filtered(lambda r: r.field_name == "state")
                    else "fields_update"
                )
            elif log.method == "create":
                log.log_category = "create"
            elif log.method == "unlink":
                log.log_category = "unlink"
