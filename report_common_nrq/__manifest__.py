# -*- coding: utf-8 -*-
# Copyright 2016-2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Report Common",
    "summary": "",
    "version": "10.0.1.7.2",
    "category": "Uncategorized",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["account", "sale", "purchase", "base_partner_number"],
    "data": [
        "data/res_partner_data.xml",
        "views/res_company_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/purchase_order_views.xml",
        "views/account_invoice_views.xml",
        "report/common_template.xml",
    ],
}
