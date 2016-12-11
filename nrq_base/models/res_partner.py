# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    delivery_notice = fields.Boolean(
        string="Delivery Notice",
        default=True,
        help="Tick if you want to print Delivery notice with invoice report.",
    )
    partner_no = fields.Char(
        string="Partner Number",
        readonly=True,
        copy=False,
    )

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(partner_no)',
         "Partner number must be unique"),
    ]

    @api.model
    def create(self, vals):
        partner_no = self.env['ir.sequence'].next_by_code('res.partner')
        vals.update({'partner_no': partner_no})
        return super(ResPartner, self).create(vals)
