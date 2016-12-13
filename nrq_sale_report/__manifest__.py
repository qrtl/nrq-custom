# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name' : 'Nrq:: Sale Report',
    'version' : '10.0.1.0.0',
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
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
