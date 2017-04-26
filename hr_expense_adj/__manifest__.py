# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Adjustments on Expense Functions",
    "summary": "",
    "description": """
* Hide "Submit to Manager" button and Account field in expense form
* Adjust expense tree view fields
* Propose a default value in expense report summary field
    """,
    "version": "10.0.1.0.0",
    "category": "HR",
    "website": "https://www.odoo-asia.com/",
    "author": "Rooms For (Hong Kong) Limited",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "",
    "post_init_hook": "",
    "post_load": "",
    "uninstall_hook": "",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "hr_expense",
    ],
    "data": [
        'views/hr_expense_views.xml',
        'views/hr_expense_sheet_views.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
