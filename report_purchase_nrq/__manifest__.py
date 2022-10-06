# -*- coding: utf-8 -*-
# Copyright 2016-2019 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Purchase Document Print",
    "summary": "",
    "version": "10.0.2.0.0",
    "category": "Purchases",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["purchase", "report_common_nrq"],
    "data": ["report/purchase_report_template.xml", "views/purchase_order_views.xml"],
}
