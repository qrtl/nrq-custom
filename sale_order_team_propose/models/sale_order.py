# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super(SaleOrder, self).onchange_partner_id()
        values = {}
        if not self.partner_id.team_id and self.partner_id.user_id:
            sale_team = self.env['crm.team'].search([
                ('member_ids.id', '=', self.partner_id.user_id.id)
            ], limit=1)
            if sale_team:
                values['team_id'] = sale_team.id
        self.update(values)
