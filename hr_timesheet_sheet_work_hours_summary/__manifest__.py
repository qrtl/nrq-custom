# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Timesheet Working Hours Summary',
    'summary': '',
    'version': '10.0.1.1.0',
    'category': 'HR',
    'website': 'https://www.quartile.co/',
    'author': 'Quartile Limited',
    'license': 'AGPL-3',
    'depends': [
        'hr_public_holidays',
        'hr_timesheet_attendance',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_timesheet_sheet_sheet_views.xml',
    ],
    'application': False,
    'installable': True,
}
