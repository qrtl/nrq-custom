# -*- coding: utf-8 -*-
# Copyright 2019-2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': "Audit Log Extension NRQ",
    'version': "10.0.1.0.1",
    'license': 'LGPL-3',
    'author': 'Quartile Limited',
    'website': 'http://www.quartile.co/',
    'category': "Tools",
    'depends': [
        'auditlog',
    ],
    'data': [
        'views/auditlog_log_views.xml',
    ],
    'application': True,
    'installable': True,
}
