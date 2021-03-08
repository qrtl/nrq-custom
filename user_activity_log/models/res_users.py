# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    track_user_activity = fields.Boolean("Track User Activity", dafault=False)

    @api.multi
    def toggle_track_user_activity(self):
        for record in self:
            record.track_user_activity = not record.track_user_activity
