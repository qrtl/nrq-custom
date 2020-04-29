# -*- coding: utf-8 -*-
# Copyright 2019-2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class L10nJpHrEmployee(common.TransactionCase):
    post_install = True

    def setUp(self):
        super(L10nJpHrEmployee, self).setUp()
        # Demo user
        self.test_user = self.env.ref('base.user_demo')
        # Employee record that linked to Demo user
        self.test_employee = self.env.ref('hr.employee_qdp')

    def test_00_create_edit_private_information(self):
        private_info = self.env['hr.private.info'].sudo(self.test_user.id).create({
            'employee_id': self.test_employee.id,
        })
        private_info.sudo(self.test_user.id).update({
            'family_name': '山田',
            'given_name': '太郎',
            'roman_family_name': 'YAMADA',
            'roman_given_name': 'TAROU',
        })

    def test_01_create_dependant_information(self):
        # AccessError was rasied before adding "readonly=True" to
        # appointment_letter_url during creation. Here we test the creation
        # of hr.dependant with demo user
        private_info = self.env['hr.private.info'].sudo(
            self.test_user.id).create({'employee_id': self.test_employee.id})
        self.env['hr.dependant'].sudo(self.test_user.id).create({
            'private_info_id': private_info.id,
            'employee_id': self.test_employee.id,
            'dependant_categ': '01_spouse',
            'gender': 'male',
            'residence_categ': 'together',
            'income': 0,
            'birthday': '2000/01/01',
            'furi_name': 'ﾔﾏﾀﾞ ﾀﾛｳ',
            'name': '山田 太郎',
        })
