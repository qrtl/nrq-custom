# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Adjustments on HR Employee Functions",
    "description": """
    """,
    "version": "10.0.1.0.0",
    "category": "HR",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr",
        "hr_contract",
        "hr_holidays",
    ],
    "data": [
        'views/hr_employee_views.xml',
    ],
}
