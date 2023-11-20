# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class SalePrint(models.Model):
    _inherit = "sale.order"

    @api.multi
    def print_quotation(self):
        self.filtered(lambda s: s.state == "draft").write({"state": "sent"})
        return self.env["report"].get_action(
            self, "report_sale_nrq.report_salequotation"
        )
