# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common


class HrEmployeeNrq(common.TransactionCase):
    post_install = True

    def setUp(self):
        super(HrEmployeeNrq, self).setUp()
        # Test Employee record
        self.test_employee = self.env.ref("hr.employee_al")
        # Create an employee officer user
        self.officer_user = self.env["res.users"].create(
            dict(
                name="Employee Officer",
                company_id=self.env.ref("base.main_company").id,
                login="eo",
                password="eo",
                email="emofficer@yourcompany.example.com",
                groups_id=[(6, 0, [self.env.ref("hr.group_hr_user").id])],
            )
        )
        # Create an employee manager user
        self.manager_user = self.env["res.users"].create(
            dict(
                name="Employee Manager",
                company_id=self.env.ref("base.main_company").id,
                login="em",
                password="em",
                email="emmanager@yourcompany.example.com",
                groups_id=[
                    (
                        6,
                        0,
                        [
                            self.env.ref(
                                "l10n_jp_hr_employee."
                                "group_employee_private_info_manage"
                            ).id,
                            self.env.ref("hr.group_hr_manager").id,
                        ],
                    )
                ],
            )
        )
        # Create hr holiday manager user
        self.holiday_manager_user = self.env["res.users"].create(
            dict(
                name="Holiday Manager",
                company_id=self.env.ref("base.main_company").id,
                login="hm",
                password="hm",
                email="homanager@yourcompany.example.com",
                groups_id=[
                    (6, 0, [self.env.ref("hr_holidays.group_hr_holidays_manager").id])
                ],
            )
        )
        # Create hr holiday record
        self.hr_holidays = self.env["hr.holidays"].create(
            dict(
                employee_id=self.test_employee.id,
                name="Test Holiday Record",
                holiday_status_id=self.env["hr.holidays.status"]
                .search([("limit", "=", False)])[0]
                .id,
                type="add",
                holiday_type="employee",
                number_of_days_temp=1,
            )
        )

    def test_00_officer_access_active_employee(self):
        self.test_employee.sudo().update({"active": True})
        self.test_employee.sudo(self.officer_user.id).read()

    def test_01_manager_access_active_employee(self):
        self.test_employee.sudo().update({"active": True})
        self.test_employee.sudo(self.manager_user.id).read()

    def test_02_officer_access_inactive_employee(self):
        self.test_employee.sudo().update({"active": False})
        self.test_employee.sudo(self.officer_user.id).read()

    def test_03_manager_access_inactive_employee(self):
        self.test_employee.sudo().update({"active": False})
        self.test_employee.sudo(self.manager_user.id).read()

    def test_04_holiday_manager_access_active_hr_holdays_record(self):
        self.test_employee.sudo().update({"active": True})
        self.hr_holidays.sudo(self.holiday_manager_user.id).read()

    def test_05_holiday_manager_access_inactive_hr_holdays_record(self):
        self.test_employee.sudo().update({"active": False})
        self.hr_holidays.sudo(self.holiday_manager_user.id).read()
