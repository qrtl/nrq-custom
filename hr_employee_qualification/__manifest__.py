# -*- coding: utf-8 -*-
# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Hr Employee Qualification",
    "description": """
    """,
    "version": "10.0.1.0.0",
    "category": "Localization",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["hr", "l10n_jp_hr_employee"],
    "data": [
        "security/res_groups.xml",
        "security/hr_security.xml",
        "views/hr_qualification_views.xml",
        "data/manuitem_data.xml",
    ],
}
