# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Accounting Document Print",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Accounting",
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
        "nrq_base",
    ],
    "data": [
        'report/common_template.xml',
        'report/account_invoice_template.xml',
        'report/account_acceptance_template.xml',
        'report/account_deliverynote_template.xml',
        'report/account_invoice_acceptance_template.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
