# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    pj_id = fields.Many2one(
        'project.project',
        string='Related Project',
        store=True,
    )
    project_partner_id = fields.Many2one(
        related='pj_id.partner_id',
        string='Customer',
        store=True,
        readonly=True,
    )
    parent_project_id = fields.Many2one(
        related='pj_id.parent_project_id',
        string='Parent Project',
        store=True,
        readonly=True,
    )

    @api.model
    def create(self, vals):
        res = super(AccountAnalyticLine, self).create(vals)
        if res.account_id.project_ids:
            for project in res.account_id.project_ids:
                res.pj_id = project.id
                return res
