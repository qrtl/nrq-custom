# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Auto-Complete Search Patch',
    'version': '10.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.quartile.co',
    'category': 'Web',
    'license': 'AGPL-3',
    'summary': "",
    'description': """
- Applying the fix batch of fixing the update search view menu on click IME suggestion menu.
https://github.com/odoo/odoo/commit/6610b5d8fffe567b2dd7e4f45815eb4643defe83
    """,
    'depends': [
        'web'
    ],
    'data': [
        'views/asset.xml',
    ],
    'installable': True,
}
