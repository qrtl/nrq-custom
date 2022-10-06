# -*- coding: utf-8 -*-
# Copyright 2019-2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Adjustments on HR Employee Functions",
    "version": "10.0.1.2.1",
    "category": "HR",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_contract",
        "hr_holidays",
        "hr_timesheet_sheet",
        "l10n_jp_hr_employee",
    ],
    "data": [
        "security/hr_security.xml",
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
    ],
}
