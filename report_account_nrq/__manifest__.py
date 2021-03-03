# -*- coding: utf-8 -*-
# Copyright 2016-2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Accounting Document Print",
    "summary": "",
    "version": "10.0.1.1.0",
    "category": "Accounting",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["account", "report_common_nrq"],
    "data": [
        "report/account_report_invoice_acceptance.xml",
        "report/account_report_deliverynote.xml",
    ],
}
