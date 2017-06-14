# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class InvoicePrint(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def invoice_print(self):
        self.ensure_one()
        self.sent = True
        return self.env['report'].get_action(
            self, 'report_account_nrq.report_invoice_acceptance')
