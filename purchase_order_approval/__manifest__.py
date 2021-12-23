# -*- coding: utf-8 -*-
# Copyright 2017-2018 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Purchase Order Approval",
    "summary": "",
    "version": "10.0.1.3.0",
    "category": "Sales",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["purchase", "report_purchase_nrq"],
    "data": [
        "data/mail_template_data.xml",
        "views/purchase_order_views.xml",
        "report/purchase_report.xml",
    ],
}
