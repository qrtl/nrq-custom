# Copyright 2024 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrQualificationType(models.Model):
    _name = "hr.qualification.type"
    _order = "sequence, id"

    name = fields.Char(required=True, help="e.g. CISA")
    sequence = fields.Integer(default=10)
    is_allowed_score = fields.Boolean(help="If enabled, allows input in the score field of the qualification.")
