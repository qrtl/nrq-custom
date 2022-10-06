# -*- coding: utf-8 -*-
# Copyright 2017-2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Adjustments on Expense Functions",
    "version": "10.0.1.4.3",
    "category": "HR",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["hr_expense", "ir_sequence_range_month"],
    "data": [
        "data/expense_data.xml",
        "views/hr_expense_views.xml",
        "views/hr_expense_sheet_views.xml",
    ],
}
