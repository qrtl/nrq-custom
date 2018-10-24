# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Invoice Lines Views",
    "summary": "",
    "description": """
- Add two list view for Customer Invoice Lines and Vedor Invoice Lines
    """,
    "version": "10.0.1.0.0",
    "category": "Account",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account"
    ],
    "data": [
        'views/account_invoice_line_views.xml',
    ],
}
