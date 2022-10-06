# -*- coding: utf-8 -*-
# Copyright 2017-2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Quotation Approval",
    "summary": "",
    "version": "10.0.1.3.1",
    "category": "Sales",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["sale", "report_sale_nrq"],
    "data": [
        "data/mail_template_data.xml",
        "views/sale_order_views.xml",
        "report/sale_report.xml",
    ],
}
