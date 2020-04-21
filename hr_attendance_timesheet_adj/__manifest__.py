# -*- coding: utf-8 -*-
# Copyright 2018-2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Adjustments on Attendance Functions',
    'summary': '',
    'description': '''
    ''',
    'version': '10.0.1.3.0',
    'category': 'HR',
    'website': 'https://www.quartile.co/',
    'author': 'Quartile Limited',
    'license': 'AGPL-3',
    'depends': [
        'hr_attendance',
        'hr_timesheet_attendance',
        'account_analytic_profit_loss_analysis',
        'hr_timesheet_sheet'
    ],
    'data': [
        'security/base_security.xml',
        'views/hr_attendance_views.xml',
        'views/hr_timesheet_sheet_sheet_views.xml',
    ],
    'application': False,
    'installable': True,
}
