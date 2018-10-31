# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.onchange('user_id')
    def onchange_user_id(self):
        values = {}
        values['team_id'] = self._get_default_team()
        if not self.partner_id.team_id:
            if self.user_id:
                sale_team = self.env['crm.team'].sudo().search([
                    '|',
                    ('user_id', '=', self.user_id.id),
                    ('member_ids.id', '=', self.user_id.id)
                ], limit=1)
                if sale_team:
                    values['team_id'] = sale_team.id
        self.update(values)
