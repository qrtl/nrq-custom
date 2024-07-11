# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Project Parent Adjust',
    'description': """
- Hide Parent Project field (expected to be temporarily).
        """,
    'version': '10.0.1.0.1',
    'license': 'AGPL-3',
    'category': 'project',
    'author': 'Quartile Limited',
    'website': 'https://www.quartile.co',
    'depends': [
        'project_parent',
    ],
    'data': [
        'views/project_project_views.xml',
    ]
}
