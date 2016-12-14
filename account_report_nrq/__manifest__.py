# # -*- coding: utf-8 -*-
# # Part of Odoo. See LICENSE file for full copyright and licensing details.
# {
#     'name' : 'Nrq:: Account Report',
#     'version' : '1.0',
#     'summary': '',
#     'description': """
# It will adds reports on invoice as below:
#     - Acceptance
#     - Delivery Notice
#     - Invoice with Acceptance and Delivery Notice
#     """,
#     'category': 'Accounting',
#     'website': 'https://www.odoo.com/page/billing',
#     'depends' : ['nrq_base'],
#     'data': [
#         'views/report_comman.xml',
#         'views/report_only_invoice.xml',
#         'views/report_acceptance.xml',
#         'views/report_delivery_note.xml',
#         'views/report_nrq_invoice.xml',
#     ],
#     'installable': True,
#     'application': False,
#     'auto_install': False,
# }

# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Accounting Document Print",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Accounting",
    "website": "https://www.odoo-asia.com/",
    "author": "Rooms For (Hong Kong) Limited T/A OSCG",
    "license": "AGPL-3",
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
        "nrq_base",
    ],
    "data": [
        'report/report_comman.xml',
        'report/report_only_invoice.xml',
        'report/report_acceptance.xml',
        'report/report_delivery_note.xml',
        'report/report_nrq_invoice.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
