# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    delivery_notice = fields.Boolean(
        string="Delivery Notice",
        default=True,
        help="Select if delivery notice should be printed together with "
             "invoice.",
    )
    partner_no = fields.Char(
        string="Partner Number",
        readonly=False,
        copy=False,
    )

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(partner_no)',
         "Partner number must be unique."),
    ]

    @api.model
    def create(self, vals):
        partner_no = self.env['ir.sequence'].next_by_code('res.partner')
        vals.update({'partner_no': partner_no})
        return super(ResPartner, self).create(vals)
