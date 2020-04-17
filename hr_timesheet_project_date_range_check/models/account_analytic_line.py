# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, models
from odoo.exceptions import ValidationError


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.one
    @api.constrains('project_id', 'date')
    def check_project_date(self):
        if self.project_id:
            if self.project_id.date_start and self.date < \
                    self.project_id.date_start or self.project_id.date and \
                    self.date > self.project_id.date:
                raise ValidationError(_(
                    'You cannot have an entry that the date is out of the '
                    'project date range'))
