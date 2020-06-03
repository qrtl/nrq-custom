# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import time
from odoo.tests import common


class TestHrTimesheetSheet(common.TransactionCase):

    def setUp(self):
        super(TestHrTimesheetSheet, self).setUp()
        self.holiday_model = self.env["hr.holidays.public"]
        self.holiday_model_line = self.env["hr.holidays.public.line"]
        self.timesheet_sheet = self.env['hr_timesheet_sheet.sheet']
        self.test_employee = self.browse_ref('hr.employee_qdp')
        self.resource_id = self.env.ref('resource.timesheet_group1')

        self.test_timesheet_sheet = self.timesheet_sheet.create({
            'date_from': time.strftime('%Y-%m-11'),
            'date_to': time.strftime('%Y-%m-17'),
            'name': 'Gilles Gravie',
            'state': 'new',
            'user_id': self.browse_ref('base.user_demo').id,
            'employee_id': self.test_employee.id,
        })

    def test_compute_works_hours(self):
        # Check Standard Hours without resource set
        self.assertEqual(self.test_timesheet_sheet.standard_work_hours, 0)
        self.test_timesheet_sheet.employee_id.write({
            'calendar_id': self.resource_id.id
        })

        # Check Standard Hours with resource set
        self.assertEqual(self.test_timesheet_sheet.standard_work_hours, 40.0,
                         "The Standard Hours did not match the with value")

        # Create holidays
        holiday2 = self.holiday_model.create({
            'year': time.strftime('%Y'),
            'country_id': self.test_employee.user_id.partner_id.country_id.id
        })
        self.holiday_model_line.create({
            'name': 'holiday 1',
            'date': time.strftime('%Y-%m-15'),
            'year_id': holiday2.id
        })
        self.test_timesheet_sheet.employee_id.write({
            'calendar_id': self.resource_id.id
        })

        # Check Holiday Hours
        self.assertEqual(self.test_timesheet_sheet.holiday_hours, 8,
                         "The Holiday Hours did not match the with value")

        # Check Expected Hours
        self.assertEqual(
            self.test_timesheet_sheet.expected_work_hours,
            self.test_timesheet_sheet.standard_work_hours -
            self.test_timesheet_sheet.holiday_hours,
            "The Expected Hours did not match the with value")

        self.test_timesheet_sheet.write({
            'timesheet_ids': [(0, 0, {
                'project_id': self.browse_ref('project.project_project_2').id,
                'date': time.strftime('%Y-%m-11'),
                'name': 'Develop yaml for hr module(2)',
                'user_id': self.browse_ref('base.user_demo').id,
                'unit_amount': 8.00,
                'product_id': self.browse_ref('product.product_product_1').id,
            })]})

        # Check Overtime Working Hours
        self.assertEqual(
            self.test_timesheet_sheet.overtime_hours,
            self.test_timesheet_sheet.total_timesheet -
            self.test_timesheet_sheet.expected_work_hours,
            "The Overtime Working Hours did not match the with value")
