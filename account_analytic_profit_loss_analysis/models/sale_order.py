# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    parent_project_id = fields.Many2one(
        'project.project',
        string='Parent Project',
        readonly=True,
        states={'draft': [('readonly', False)]},
    )

    @api.multi
    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        for order in self:
            if order.project_project_id:
                order.project_project_id.parent_project_id = \
                    order.parent_project_id
        return True
