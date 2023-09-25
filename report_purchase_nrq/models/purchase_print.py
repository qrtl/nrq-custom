# -*- coding: utf-8 -*-
# Copyright 2016-2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchasePrint(models.Model):
    _inherit = "purchase.order"

    display_tax = fields.Boolean("Display Tax",)

    @api.multi
    def print_quotation(self):
        self.write({"state": "sent"})
        return self.env["report"].get_action(
            self, "report_purchase_nrq.report_purchaseorder"
        )
