# -*- coding: utf-8 -*-
# Copyright 2016-2018 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sales Document Print",
    "summary": "",
    "version": "10.0.1.3.0",
    "category": "Sales",
    "website": "https://www.odoo-asia.com/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["sale", "report_common_nrq"],
    "data": ["views/res_company_views.xml", "report/sale_report_quotation.xml"],
}
