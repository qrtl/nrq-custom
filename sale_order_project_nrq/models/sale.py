# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_project_vals(self):
        self.ensure_one()
        name = u" %s - %s" % (
            self.name,
            self.doc_title
        )
        return {
            'user_id': self.user_id.id,
            'name': name,
            'partner_id': self.partner_id.id,
            'allow_timesheets': False,
        }

    @api.multi
    def write(self, vals):
        if 'state' in vals and vals['state'] in ('sale', 'cancel'):
            for order in self:
                if order.project_project_id:
                    order.update_project_allow_timesheets(vals['state'])
        return super(SaleOrder, self).write(vals)

    def update_project_allow_timesheets(self, state):
        if state == 'sale':
            self.project_project_id.allow_timesheets = True
        if state == 'cancel':
            related_sales_orders = self.search([
                ('project_id', '=',
                 self.project_project_id.analytic_account_id.id),
                ('state', '!=', 'cancel'),
                ('id', '!=', self.id),
            ])
            if not related_sales_orders:
                self.project_project_id.allow_timesheets = False
