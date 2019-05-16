# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    appointment_letter_url = fields.Char('Letter of Appointment Link('
                                         'Dependant)')

    @api.multi
    def write(self, vals):
        #FIXME: Not the best way to handle, when hr.dependant is
        #       created/updated, the write method is triggered and pass
        #       'appointment_letter_url' to update the res.company record
        #       that would lead to a permission error.
        if 'appointment_letter_url' in vals and not \
            self.env.user.has_group('base.group_system'):
            vals.pop('appointment_letter_url')
        if vals:
            return super(ResCompany, self).write(vals)
