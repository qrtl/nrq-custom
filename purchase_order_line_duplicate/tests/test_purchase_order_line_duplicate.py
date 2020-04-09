# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from odoo.tests import common
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class PurchaseOrderLineDuplicate(common.TransactionCase):
    post_install = True

    def setUp(self):
        super(PurchaseOrderLineDuplicate, self).setUp()
        # Demo user
        self.test_user = self.env.ref('base.user_demo')

    def test_00_duplicate_order_line(self):
        self.partner_id = self.env.ref('base.res_partner_1')
        self.product_id = self.env.ref('product.product_product_8')
        po = self.env['purchase.order'].create(
            {'partner_id': self.partner_id.id})
        po_line_vals = {
            'name': self.product_id.name,
            'product_id': self.product_id.id,
            'product_qty': 5.0,
            'product_uom': self.product_id.uom_po_id.id,
            'price_unit': 500.0,
            'date_planned': datetime.today().strftime(
                DEFAULT_SERVER_DATETIME_FORMAT),
            'order_id': po.id,
        }
        po_line = self.env['purchase.order.line'].create(po_line_vals)
        # First Duplicate
        po_line.action_duplicate_line()
        self.assertEqual(len(po.order_line), 2)
        self.assertEqual(po.amount_total, 5000)
        # Second Duplicate
        po_line.action_duplicate_line()
        self.assertEqual(len(po.order_line), 3)
        self.assertEqual(po.amount_total, 7500)
