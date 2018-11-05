# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Adjustments on Sales Functions",
    "summary": "",
    "description": """
- Show Project Manager in the list and form view
- Show Untaxed Amount in the list view
- Show Confirmation Date instead of order date in the list view
    """,
    "version": "10.0.1.1.0",
    "category": "Sales",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale",
        "sale_timesheet",
        "sale_quotation_approval",
        "account_analytic_profit_loss_analysis",
    ],
    "data": [
        'views/sale_order_views.xml',
    ],
}
