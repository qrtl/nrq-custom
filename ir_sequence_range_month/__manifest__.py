# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Auto-create monthly date ranges for sequence",
    "summary": "",
    "description": """
* Odoo's sequence engine by defauld does not support refreshing 'next number'
on monthly basis.  This module adds thel logic to support it.
    """,
    "version": "10.0.1.0.0",
    "category": "Technical Settings",
    "website": "https://www.odoo-asia.com/",
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
        "base",
    ],
    "data": [
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
