# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Web Responsive Disable Search',
    'version': '10.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.quartile.co',
    'category': 'Website',
    'license': 'AGPL-3',
    'summary': "",
    'description': """
- Disable the search feature in web_responsive
  - Hide the search icon in the menu
    """,
    'depends': [
        'web_responsive'
    ],
    'data': [
        'views/asset.xml',
        'views/web.xml',
    ],
    'installable': True,
}
