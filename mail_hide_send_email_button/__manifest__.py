# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Hiding 'Send by Email' button",
    "version": "10.0.1.0.0",
    "category": "Base",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["account", "purchase", "sale"],
    "data": [
        "views/account_invoice_views.xml",
        "views/purchase_order_views.xml",
        "views/sale_order_views.xml",
    ],
}
