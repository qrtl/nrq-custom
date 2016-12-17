# -*- coding: utf-8 -*-
# Copyright 2016 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Partner Number',
    "version": "10.0.1.0.0",
    "summary": "",
    'description': """
            """,
    'category': 'Base',
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
    'depends': [
        'base',
    ],
    'data': [
        'data/res_partner_data.xml',
        'views/res_partner_views.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
