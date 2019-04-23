# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Extension to Employees for Japan",
    "description": """
    """,
    "version": "10.0.1.0.0",
    "category": "Localization",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr",
        "hr_contract",
    ],
    'external_dependencies': {
        'python': ['jaconv'],
    },
    "data": [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/hr_security.xml',
        'data/hr_employment_type_data.xml',
        'data/hr_contract_data.xml',
        'data/mail_template_data.xml',
        'views/hr_private_info_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_qualification_views.xml',
        'views/hr_dependant_views.xml',
        'views/res_company_views.xml',
    ],
}
