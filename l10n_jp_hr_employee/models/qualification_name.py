# Copyright 2024 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class QualificationName(models.Model):
    _name = "qualification.name"
    _order = "sequence, id"

    name = fields.Char(required=True, help="e.g. CISA")
    sequence = fields.Integer(default=10)
