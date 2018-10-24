# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Link Sales Order to Purchase Order and Vendor Bills",
    "summary": "",
    "description": """
- Add sale_ids to purchase order and account invoice.
- Add filters to the list views of purchase order and account invoice.
    """,
    "version": "10.0.1.0.0",
    "category": "Sales",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "purchase",
        "sale",
        "sale_timesheet",
    ],
    "data": [
        "views/account_invoice_views.xml",
        "views/purchase_order_views.xml",
    ],
}
