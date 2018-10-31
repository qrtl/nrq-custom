# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Propose Sales Order's Sales Team",
    "summary": "",
    "description": """
- Show sales team in partner form view
- Propose sales order's sales team according to customer's setting or the
salesperson setting
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
        "crm",
    ],
    "data": [
        'views/res_partner_views.xml',
    ],
}
