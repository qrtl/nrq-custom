# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common
from odoo.exceptions import ValidationError


class L10nJpHrEmployee(common.TransactionCase):

    def setUp(self):
        super(L10nJpHrEmployee, self).setUp()
        # Demo user
        self.test_user = self.env.ref('base.user_demo')
        # Employee record that linked to Demo user
        self.test_employee = self.env.ref('hr.employee_qdp')
        # Japan
        self.japan = self.env.ref('base.jp')

    def test_00_create_private_information(self):
        with self.assertRaises(ValidationError):
            self.env['hr.private.info'].sudo(self.test_user.id).create({
                'employee_id': self.test_employee.id,
                'temp_save': False,
                'private_country_id': self.japan.id,
                'roman_family_name': '山田',
                'roman_given_name': '太郎',
                'birthday': '2005/03/01',
                'gender': 'male',
                'private_phone': '09011112222',
                'private_email': 'test@test.com',
                'postal_code': '1020082',
                'address_pref': 'Tokyo',
                'address_street': '千代田区一番町１０－２２',
                'building': '千代田一番町郵便局',
                'residence_cert': False,
                'residence_cert_filename': False,
                'furi_address': 'チヨダク イチバンチョウ１０－２２',
                'furi_building': 'チヨダイチバンチョウユウビンキョク',
                'emerg_contact_type': 'spouse',
                'emerg_contact_desc': False,
                'emerg_contact_name': '山田　○○',
                'emerg_contact_postal_code': '1020082',
                'emerg_contact_address': '千代田区一番町１０－２２',
                'emerg_contact_phone': '09011112222',
                'bank_name': '三井住友銀行',
                'bank_branch': '神保町支店',
                'bank_acc_type': 'savings',
                'bank_acc_number': '1234567',
                'furi_bank_acc_holder': 'ﾔﾏﾀﾞﾀﾛｳ',
                'school_name': '○○大学',
                'school_dept_name': '○○学部○○○学科',
                'school_completion': 'completed',
                'school_completion_desc': False,
                'year_left_school': '2000',
                'qualification_ids': False,
                'pension_code': '9999',
                'pension_seq': '999999',
                'emp_ins_number_1st': '9999',
                'emp_ins_number_2nd': '999999',
                'emp_ins_number_3rd': '9',
                'note': 'Test',
                'visa_number': False,
                'date_visa_expiry': False,
                'work_permit_number': False,
                'residence_card': False,
                'residence_card_filename': False,
                'state': 'draft',
            })
