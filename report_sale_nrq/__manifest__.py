# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sales Document Print",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Sales",
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
        "sale",
        "report_common_nrq",
    ],
    "data": [
        'report/sale_report_quotation.xml'
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
