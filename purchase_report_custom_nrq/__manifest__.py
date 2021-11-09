# -*- coding: utf-8 -*-
# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Purchase Document Custom",
    "version": "10.0.1.0.0",
    "category": "Purchase",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["report_purhcase_nrq"],
    "data": [
        "report/purchase_order_report_templates.xml",
        "views/purchase_order_views.xml"
    ],
}
