# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import pytz
from odoo import api, fields, models
from odoo.http import request
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class AuditlogLog(models.Model):
    _inherit = 'auditlog.log'

    log_category = fields.Selection([
        ('state_update', 'Submitted/Set back to Draft'),
        ('fields_update', 'Fields Update'),
        ('create', 'Record Created'),
        ('unlink', 'Record Unlinked'),
        ('other', 'N/A')],
        string='Log Category',
        compute='_get_log_category',
        store=True,
    )

    @api.multi
    @api.depends('line_ids')
    def _get_log_category(self):
        for log in self:
            log.log_category = 'other'
            if log.method == 'write' and log.line_ids:
                log.log_category = 'state_update' if log.line_ids.filtered(
                    lambda r: r.field_name == 'state') else 'fields_update'
            elif log.method == 'create':
                log.log_category = 'create'
            elif log.method == 'unlink':
                log.log_category = 'unlink'


class AuditlogLogLine(models.Model):
    _inherit = 'auditlog.log.line'

    @api.model
    def create(self, vals):
        if vals.get('new_value_text') or vals.get('old_value_text'):
            old_value_text, new_value_text = vals.get(
                'old_value_text'), vals.get('new_value_text')
            user_id = self.env['res.users'].browse(request.uid)
            tz = user_id.partner_id.tz
            timezone = pytz.timezone(tz or 'UTC')
            try:
                new_value_text = pytz.UTC.localize(fields.Datetime.from_string(
                    new_value_text))
                new_value_text = new_value_text.replace(
                    tzinfo=pytz.timezone('UTC')).astimezone(timezone)
                vals.update({
                    'new_value_text': new_value_text.strftime(
                        DEFAULT_SERVER_DATETIME_FORMAT)
                })
            except ValueError:
                pass
            try:
                old_value_text = pytz.UTC.localize(fields.Datetime.from_string(
                    old_value_text))
                old_value_text = old_value_text.replace(
                    tzinfo=pytz.timezone('UTC')).astimezone(timezone)
                vals.update({
                    'old_value_text': old_value_text.strftime(
                        DEFAULT_SERVER_DATETIME_FORMAT)
                })
            except ValueError:
                pass
        return super(AuditlogLogLine, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('new_value_text') or vals.get('old_value_text'):
            old_value_text, new_value_text = vals.get(
                'old_value_text'), vals.get('new_value_text')
            user_id = self.env['res.users'].browse(request.uid)
            tz = user_id.partner_id.tz
            timezone = pytz.timezone(tz or 'UTC')
            try:
                new_value_text = pytz.UTC.localize(fields.Datetime.from_string(
                    new_value_text))
                new_value_text = new_value_text.replace(
                    tzinfo=pytz.timezone('UTC')).astimezone(timezone)
                vals.update({
                    'new_value_text': new_value_text.strftime(
                        DEFAULT_SERVER_DATETIME_FORMAT)
                })
            except ValueError:
                pass
            try:
                old_value_text = pytz.UTC.localize(fields.Datetime.from_string(
                    old_value_text))
                old_value_text = old_value_text.replace(
                    tzinfo=pytz.timezone('UTC')).astimezone(timezone)
                vals.update({
                    'old_value_text': old_value_text.strftime(
                        DEFAULT_SERVER_DATETIME_FORMAT)
                })
            except ValueError:
                pass
        return super(AuditlogLogLine, self).write(vals)
