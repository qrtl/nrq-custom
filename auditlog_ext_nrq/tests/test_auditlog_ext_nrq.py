# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID
from odoo.tests import common


class TestAuditlogExtNrq(common.TransactionCase):
    post_install = True

    def setUp(self):
        super(TestAuditlogExtNrq, self).setUp()
        self.translation_model_id = self.env.ref("base.model_ir_translation").id
        self.translation_rule = self.env["auditlog.rule"].create(
            {
                "name": "Test rule for translation",
                "model_id": self.translation_model_id,
                "log_read": True,
                "log_create": True,
                "log_write": True,
                "log_unlink": True,
                "state": "subscribed",
                "log_type": "full",
            }
        )
        self.translation_record = self.env["ir.translation"].create(
            dict(name="Test Translation Record")
        )

    def test_00_create_record(self):
        log = self.env["auditlog.log"].search(
            [
                ("model_id", "=", self.translation_model_id),
                ("method", "=", "create"),
                ("res_id", "=", self.translation_record.id),
            ],
            limit=1,
            order="id desc",
        )
        self.assertEqual(log.log_category, "create")

    def test_01_update_record_with_state(self):
        self.translation_record.update({"state": "translated"})
        log = self.env["auditlog.log"].search(
            [
                ("model_id", "=", self.translation_model_id),
                ("method", "=", "write"),
                ("res_id", "=", self.translation_record.id),
            ],
            limit=1,
            order="id desc",
        )
        self.assertEqual(log.log_category, "state_update")

    def test_02_update_record_without_state(self):
        self.translation_record.update({"name": "Test Translation Reord 2"})
        log = self.env["auditlog.log"].search(
            [
                ("model_id", "=", self.translation_model_id),
                ("method", "=", "write"),
                ("res_id", "=", self.translation_record.id),
            ],
            limit=1,
            order="id desc",
        )
        self.assertEqual(log.log_category, "fields_update")

    def test_03_unlink_record(self):
        self.translation_record.unlink()
        log = self.env["auditlog.log"].search(
            [
                ("model_id", "=", self.translation_model_id),
                ("method", "=", "unlink"),
                ("res_id", "=", self.translation_record.id),
            ],
            limit=1,
            order="id desc",
        )
        self.assertEqual(log.log_category, "unlink")

    def test_04_create_vals(self):
        """
            Test old value text,new value text with datetime field data
            Test old value text,new value text without datetime field data
        """
        # Japan is 9 hours ahead of UTC.
        self.env["res.users"].browse(SUPERUSER_ID).write({"tz": "Japan"})

        field_id = self.env.ref("base.field_ir_cron_nextcall")
        audit_log_line = self.env["auditlog.log.line"]
        audit_log_line_01 = audit_log_line.sudo().create(
            {
                "field_id": field_id.id,
                "old_value_text": "2020-01-01 01:00:00",
                "new_value_text": "2020-01-02 01:00:00",
            }
        )

        # Check the old value data updated based on superuser timezone.
        self.assertEqual(audit_log_line_01.old_value_text, "2020-01-01 10:00:00")

        # Check the new value data updated based on superuser timezone.
        self.assertEqual(audit_log_line_01.new_value_text, "2020-01-02 10:00:00")

        old_value_text = "Test Name"
        new_value_text = "Updated Test Name"
        field_id = self.env.ref("base.field_ir_cron_name")
        audit_log_line_02 = audit_log_line.sudo().create(
            {
                "field_id": field_id.id,
                "old_value_text": old_value_text,
                "new_value_text": new_value_text,
            }
        )
        # Check the old value data without datetime data, Exception Case.
        self.assertEqual(audit_log_line_02.old_value_text, old_value_text)

        # Check the new value data without datetime data, Exception Case.
        self.assertEqual(audit_log_line_02.new_value_text, new_value_text)
