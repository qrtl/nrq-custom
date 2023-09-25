# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestAccountInvoiceParterNumber(common.SavepointCase):
    def setUp(self):
        super(TestAccountInvoiceParterNumber, self).setUp()
        self.invoice_account = self.env['account.account'].search(
            [('user_type_id',
              '=',
              self.env.ref('account.data_account_type_receivable').id
              )], limit=1)
        self.partner = self.env.ref('base.res_partner_1')

    def test_account_invoice_partner_number(self):
        self.assertFalse(self.partner.parnter_no)
        invoice = self.env['account.invoice'].create({
            'partner_id': self.partner.id,
            'account_id': self.invoice_account.id,
            'type': 'out_invoice',
        })
        self.assertFalse(invoice.partner_no)
        
        self.partner.write({'parnter_no': '123'})
        invoice = self.env['account.invoice'].create({
            'partner_id': self.partner.id,
            'account_id': self.invoice_account.id,
            'type': 'out_invoice',
        })
        self.assertEqual(invoice.partner_no, '000123')
