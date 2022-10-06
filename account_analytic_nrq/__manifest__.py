# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Adjustments on Account Analytic Functions",
    "summary": "",
    "description": """
* Add partner_id of the move_id to account.analytic.line
* Adjust the list view of the account.analytic.line
    """,
    "version": "10.0.1.0.0",
    "category": "Accounting",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["account"],
    "data": ["views/account_analytic_line_views.xml"],
}
