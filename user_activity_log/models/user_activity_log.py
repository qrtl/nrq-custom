# -*- coding: utf-8 -*-
# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import json

from odoo import api, fields, models
from werkzeug.urls import url_encode


class UserActivityLog(models.Model):
    _name = 'user.activity.log'
    _order = "create_date desc"

    name = fields.Char("Record", compute='compute_record_name')
    model = fields.Char("Model")
    res_id = fields.Char("Record ID")
    user_id = fields.Many2one("res.users", "User")
    method = fields.Char('Method')
    log_details = fields.Text("Log Details")

    @api.multi
    def compute_record_name(self):
        for log in self:
            if log.model and log.res_id:
                try:
                    record = self.env[log.model].sudo().browse(log.res_id)
                    log.name = record.name_get()[0][1]
                except Exception:
                    pass

    @api.model
    def get_record(self, model, res_id):
        return self.env[model].sudo().browse(res_id)

    @api.model
    def create_activity_log(self, model, method, recs, args):
        user = self.env.user
        if user.track_user_activity and self._name != model._name:
            argments = json.dumps(args, ensure_ascii=False, encoding='utf8')
            for rec in recs:
                self.sudo().create({
                    'model': model._name,
                    'method': method,
                    'user_id': user.id,
                    'res_id': rec.id,
                    'log_details': argments
                })
            else:
                self.sudo().create({
                    'model': model._name,
                    'method': method,
                    'user_id': user.id,
                    'res_id': False,
                    'log_details': argments
                })

    @api.multi
    def open_record(self):
        for log in self:
            if log.model and log.res_id:
                params = {
                    'model': log.model,
                    'res_id': log.res_id,
                }
                record = self.env[log.model].browse(log.res_id)
                return {
                    'type': 'ir.actions.act_url',
                    'url': '/mail/view?' + url_encode(params),
                    'target': 'self',
                    'target_type': 'public',
                    'res_id': record.id,
                }
