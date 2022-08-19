# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
import logging

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    partner_no = fields.Char(string='Partner Number', readonly=True, store=True, compute='_compute_partner_number')

    @api.depends('partner_id')
    def _compute_partner_number(self):
        logging.info("Call Compute Function")
        for rec in self:
            if rec.partner_id and rec.partner_id.partner_no:
                if len(rec.partner_id.partner_no) < 6:
                    length = 6 - len(rec.partner_id.partner_no)
                    p_no = rec.partner_id.partner_no
                    for i in range(0, length):
                        p_no = '0' + p_no
                    rec.partner_no = p_no
                else:
                    rec.partner_no = rec.partner_id.partner_no
            else:
                rec.partner_no = ""

    def _change_partner_number(self, partner_no):
        if partner_no:
            if len(partner_no) < 6:
                length = 6 - len(partner_no)
                p_no = partner_no
                for i in range(0, length):
                    p_no = '0' + p_no
                self.partner_no = p_no
            else:
                self.partner_no = partner_no
        else:
            self.partner_no = ""


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange('partner_no')
    def onchange_partner_no(self):
        account_invoices = self.env['account.invoice'].search([('partner_id', '=', self._origin.id)])
        logging.info("Onchange function++++++++++++")
        logging.info(self.id)
        if account_invoices:
            logging.info("Account move________________")
            for invoice in account_invoices:
                logging.info("Inside If loop")
                invoice._change_partner_number(self.partner_no)
