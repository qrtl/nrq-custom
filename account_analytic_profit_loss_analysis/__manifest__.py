# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Analytic Account Profit and Loss Analysis",
    "summary": "",
    "description": """""",
    "version": "10.0.1.1.0",
    "category": "Accounting",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        'account',
        'project_parent',
        'sale_timesheet',
        'hr_timesheet_sheet',
        'hr_expense'
    ],
    "data": [
        'data/analytic_type_data.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/analytic_type_views.xml',
        'views/account_account_views.xml',
        'views/account_analytic_line_views.xml',
        'views/hr_timesheet_sheet_views.xml',
        'views/project_timesheet_view.xml',
        'views/hr_expense_views.xml',
    ],
}
