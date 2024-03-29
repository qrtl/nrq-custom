# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

try:
    import jaconv
except ImportError:
    pass

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HrQualification(models.Model):
    _name = "hr.qualification"
    _order = "date_obtained"

    name = fields.Char(required=True, help="e.g. CISA",)
    private_info_id = fields.Many2one("hr.private.info", string="Private Info",)
    employee_id = fields.Many2one(related="private_info_id.employee_id", store=True,)
    date_obtained = fields.Char("Date Obtained", required=True,)
    date_expiry = fields.Date("Valid Until",)
    reference = fields.Char()
    qualification_file = fields.Binary("Attachment",)
    qualification_file_filename = fields.Char("Attachment File Name",)

    @api.onchange("date_obtained")
    def _onchange_date_obtained(self):
        if self.date_obtained:
            self.date_obtained = jaconv.z2h(
                self.date_obtained.replace("-", "/"), ascii=True, digit=True
            )

    @api.constrains("date_obtained")
    def _check_date_obtained(self):
        for rec in self:
            msg = _("%s seems to be incorrect.")
            if rec.date_obtained:
                date = (
                    rec.date_obtained + "/01"
                    if len(rec.date_obtained) == 7
                    else rec.date_obtained
                )
                try:
                    fields.Date.from_string(date.replace("/", "-"))
                except Exception:
                    raise ValidationError(msg % _("Date Obtained"))
                if len(rec.date_obtained) not in [7, 10]:
                    raise ValidationError(
                        _(
                            "Please adjust the format to be "
                            "'YYYY/MM/DD' or 'YYYY/MM'."
                        )
                    )
