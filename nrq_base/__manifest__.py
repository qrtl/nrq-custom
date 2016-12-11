# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Nrq:: Base',
    'version': '1.0',
    'summary': '',
    'description': """
It will adds custom fields on Sales Order, Invoice and Partner.
    """,
    'category': 'Accounting',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['account', 'sale'],
    'data': [
        'data/res_partner_data.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
