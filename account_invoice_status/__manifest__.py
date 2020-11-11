# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Account Invoice Status",
    "summary": "Make the invoice validation operation easier",
    "version": "10.0.1.1.0",
    "category": "Accounting",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "",
    "post_init_hook": "",
    "post_load": "",
    "uninstall_hook": "",
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["account"],
    "data": ["views/account_invoice_view.xml"],
    "demo": [],
    "qweb": [],
}
