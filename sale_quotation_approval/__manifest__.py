# -*- coding: utf-8 -*-
# Copyright 2017-2018 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Quotation Approval",
    "summary": "",
    "version": "10.0.1.2.0",
    "category": "Sales",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
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
        "report_sale_nrq",
    ],
    "data": [
        'views/sale_order_views.xml',
        'report/sale_report.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
