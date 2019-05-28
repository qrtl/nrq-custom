# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common
from odoo.exceptions import AccessError


class HrEmployeeNrq(common.TransactionCase):
    post_install = True

    def setUp(self):
        super(HrEmployeeNrq, self).setUp()
        # Test Employee record
        self.test_employee = self.env.ref('hr.employee_al')
        # Create an employee officer user
        self.officer_user = self.env['res.users'].create(dict(
            name="Employee Officer",
            company_id=self.env.ref('base.main_company').id,
            login="eo",
            password="eo",
            email="emofficer@yourcompany.example.com",
            groups_id=[(6, 0, [self.env.ref('hr.group_hr_user').id])]
        ))
        # Create an employee manager user
        self.manager_user = self.env['res.users'].create(dict(
            name="Employee Manager",
            company_id=self.env.ref('base.main_company').id,
            login="em",
            password="em",
            email="emmanager@yourcompany.example.com",
            groups_id=[(6, 0, [
                self.env.ref(
                    'l10n_jp_hr_employee.group_employee_private_info_manage').id,
                self.env.ref('hr.group_hr_manager').id
            ])]
        ))

    def test_00_officer_access_active_employee(self):
        self.test_employee.sudo().update({
            'active': True,
        })
        self.test_employee.sudo(self.officer_user.id).read()

    def test_01_manager_access_active_employee(self):
        self.test_employee.sudo().update({
            'active': True,
        })
        self.test_employee.sudo(self.manager_user.id).read()

    def test_02_officer_access_inactive_employee(self):
        with self.assertRaises(AccessError):
            self.test_employee.sudo().update({
                'active': False,
            })
            self.test_employee.sudo(self.officer_user.id).read()

    def test_03_manager_access_inactive_employee(self):
        self.test_employee.sudo().update({
            'active': False,
        })
        self.test_employee.sudo(self.manager_user.id).read()
