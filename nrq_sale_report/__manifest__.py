# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Nrq:: Sale Report',
    'version' : '1.0',
    'summary': '',
    'description': """
It will adds report on sales order as below:
    - Sales Order with Tax Information
    - Sales Order without Tax Information
    """,
    'category': 'Sales',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['nrq_base'],
    'data': [
        'views/report_sale_with_tax.xml',
        'views/report_sale_without_tax.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
