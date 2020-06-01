# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common


class TestAuditlogExtNrq(common.TransactionCase):
    post_install = True

    def setUp(self):
        super(TestAuditlogExtNrq, self).setUp()
        self.translation_model_id = self.env.ref(
            'base.model_ir_translation').id
        self.translation_rule = self.env['auditlog.rule'].create({
            'name': 'Test rule for translation',
            'model_id': self.translation_model_id,
            'log_read': True,
            'log_create': True,
            'log_write': True,
            'log_unlink': True,
            'state': 'subscribed',
            'log_type': 'full',
        })
        self.translation_record = self.env['ir.translation'].create(dict(
            name="Test Translation Record"
        ))

    def test_00_create_record(self):
        log = self.env['auditlog.log'].search([
            ('model_id', '=', self.translation_model_id),
            ('method', '=', 'create'),
            ('res_id', '=', self.translation_record.id),
        ], limit=1, order='id desc')
        self.assertEqual(log.log_category, 'create')

    def test_01_update_record_with_state(self):
        self.translation_record.update({
            'state': 'translated'
        })
        log = self.env['auditlog.log'].search([
            ('model_id', '=', self.translation_model_id),
            ('method', '=', 'write'),
            ('res_id', '=', self.translation_record.id),
        ], limit=1, order='id desc')
        self.assertEqual(log.log_category, 'state_update')

    def test_02_update_record_without_state(self):
        self.translation_record.update({
            'name': 'Test Translation Reord 2'
        })
        log = self.env['auditlog.log'].search([
            ('model_id', '=', self.translation_model_id),
            ('method', '=', 'write'),
            ('res_id', '=', self.translation_record.id),
        ], limit=1, order='id desc')
        self.assertEqual(log.log_category, 'fields_update')

    def test_03_unlink_record(self):
        self.translation_record.unlink()
        log = self.env['auditlog.log'].search([
            ('model_id', '=', self.translation_model_id),
            ('method', '=', 'unlink'),
            ('res_id', '=', self.translation_record.id),
        ], limit=1, order='id desc')
        self.assertEqual(log.log_category, 'unlink')
