# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    pj_id = fields.Many2one(
        'project.project',
        string='Related Project',
        compute='_compute_pj_id',
        inverse='_set_account_id',
    )
    parent_project_id = fields.Many2one(
        related='pj_id.parent_project_id',
        string='Parent Project',
        store=True,
        readonly=True,
    )

    @api.multi
    @api.depends('account_id')
    def _compute_pj_id(self):
        for line in self:
            if line.account_id and line.account_id.project_ids:
                for project in line.account_id.project_ids:
                    line.pj_id = project.id

    @api.multi
    def _set_account_id(self):
        for line in self:
            line.account_id = line.pj_id.account_id.id
