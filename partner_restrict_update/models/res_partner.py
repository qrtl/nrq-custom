# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _raise_error(self):
        raise UserError(
            _("You do not have the permission to create/edit partner records.")
        )

    @api.model
    def create(self, vals):
        if not self.env.user.has_group("base.group_partner_manager"):
            self._raise_error()
        return super(ResPartner, self).create(vals)

    @api.multi
    def write(self, vals):
        user = self.env.user
        if self.filtered(lambda x: x != user.partner_id) and not user.has_group(
            "base.group_partner_manager"
        ):
            self._raise_error()
        return super(ResPartner, self).write(vals)
