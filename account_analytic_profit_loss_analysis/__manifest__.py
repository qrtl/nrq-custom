# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Analytic Account Profit and Loss Analysis",
    "summary": "",
    "description": """""",
    "version": "10.0.1.0.1",
    "category": "Accounting",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "project_parent",
        "sale_timesheet",
    ],
    "data": [
        "views/account_analytic_line_views.xml",
        "views/sale_order_views.xml",
    ],
}
