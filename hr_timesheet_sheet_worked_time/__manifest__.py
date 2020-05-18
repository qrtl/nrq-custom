# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'HR Timesheet Worked Time',
    'summary': '',
    'description': '''
    ''',
    'version': '10.0.1.0.0',
    'category': 'HR',
    'website': 'https://www.quartile.co/',
    'author': 'Quartile Limited',
    'license': 'LGPL-3',
    'depends': [
        'hr_timesheet_attendance',
        'hr_public_holidays',
    ],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'application': False,
    'installable': True,
}
