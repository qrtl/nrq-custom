# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Duplicate Sales Order Lines",
    "summary": "",
    "description": """
- Add "Duplicate Order Lines" button to sale order form view that will 
duplicate the order lines in the sales order.
    """,
    "version": "10.0.1.0.0",
    "category": "Sales",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale",
    ],
    "data": [
        'views/sale_order_views.xml',
    ],
}
