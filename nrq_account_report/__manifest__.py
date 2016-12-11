# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Nrq:: Account Report',
    'version' : '1.0',
    'summary': '',
    'description': """
It will adds reports on invoice as below:
    - Acceptance
    - Delivery Notice
    - Invoice with Acceptance and Delivery Notice
    """,
    'category': 'Accounting',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['nrq_base'],
    'data': [
        'views/report_comman.xml',
        'views/report_only_invoice.xml',
        'views/report_acceptance.xml',
        'views/report_delivery_note.xml',
        'views/report_nrq_invoice.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
