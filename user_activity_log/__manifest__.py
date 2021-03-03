# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "User Activity Log",
    "category": "Extra Tools",
    "version": "10.0.1.0.0",
    "author": "Quartile Limited, Aktiv Software",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": ["base"],
    "data": [
        "data/ir_cron.xml",
        "security/ir.model.access.csv",
        "views/user_activity_log_views.xml",
        "views/res_users_views.xml",
    ],
    "installable": True,
    "application": False,
}
