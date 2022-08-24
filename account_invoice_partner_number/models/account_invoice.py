# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    partner_no = fields.Char(
        string="Partner Number",
        readonly=True,
        store=True,
        compute="_compute_partner_no",
    )

    # We apply padding for better sorting and searchability.
    # i.e. there can be '999' and '1111' for partner_no of res.partner
    # records and sorting does not yield the expected result without padding.
    @api.depends("commercial_partner_id", "commercial_partner_id.partner_no")
    def _compute_partner_no(self):
        for rec in self:
            partner = rec.commercial_partner_id
            if partner and partner.partner_no:
                rec.partner_no = partner.partner_no.zfill(6)
