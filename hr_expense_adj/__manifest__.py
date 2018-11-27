# -*- coding: utf-8 -*-
# Copyright 2017-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Adjustments on Expense Functions",
    "summary": "",
    "description": """
* Hides "Submit to Manager" button and Account field in expense form
* Proposes default values in expense report summary field
* Adds 'draft' state to expense report
    """,
    "version": "10.0.1.4.0",
    "category": "HR",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_expense",
        "ir_sequence_range_month",
    ],
    "data": [
        'data/expense_data.xml',
        'views/hr_expense_views.xml',
        'views/hr_expense_sheet_views.xml',
    ],
}
