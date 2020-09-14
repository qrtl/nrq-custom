# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Employee Compute Leave Days Adjustments',
    'summary': '',
    'version': '10.0.1.0.0',
    'category': 'HR',
    'website': 'https://www.quartile.co/',
    'author': 'Quartile Limited',
    'license': 'AGPL-3',
    'depends': [
        'hr_holidays_compute_days',
    ],
    'data': [
        'views/hr_holidays_views.xml'
    ],
    'application': False,
    'installable': True,
}
