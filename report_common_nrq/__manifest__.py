# -*- coding: utf-8 -*-
# Copyright 2016-2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Report Common",
    "summary": "",
    "version": "10.0.1.4.0",
    "category": "Uncategorized",
    "website": "https://www.odoo-asia.com/",
    "author": "Rooms For (Hong Kong) Limited T/A OSCG",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "",
    "post_init_hook": "",
    "post_load": "",
    "uninstall_hook": "",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "account",
        "sale",
        "purchase",
        "base_partner_number",
    ],
    "data": [
        'data/res_partner_data.xml',
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/account_invoice_views.xml',
        'report/common_template.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}