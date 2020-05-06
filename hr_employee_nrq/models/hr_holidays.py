# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from datetime import timedelta

from odoo import _, api, fields, models
from odoo.addons.hr_holidays.models.hr_holidays import HOURS_PER_DAY


class HrHolidays(models.Model):
    _inherit = 'hr.holidays'

    @api.multi
    def _compute_can_reset(self):
        """ User can reset a leave request if it is its own leave request
            or if he is an Hr Manager.
        """
        user = self.env.user
        group_hr_manager = self.env.ref(
            'hr_holidays.group_hr_holidays_manager')
        for holiday in self:
            # QTL Modify
            # Added sudo() to access employee's field
            if group_hr_manager in user.groups_id or holiday.employee_id and\
                    holiday.employee_id.sudo().user_id == user:
                holiday.can_reset = True

    @api.multi
    def name_get(self):
        res = []
        for leave in self:
            # QTL Modify
            # Add sudo() to access employee's field
            res.append((leave.id, _("%s on %s : %.2f day(s)") % (
                leave.employee_id.sudo().name or leave.category_id.name,
                leave.holiday_status_id.name, leave.number_of_days_temp)))
        return res

    @api.onchange('date_from')
    def _onchange_date_from(self):
        """ If there are no date set for date_to,
            automatically set one 8 hours later than
            the date_from. Also update the number_of_days.
        """
        date_from = self.date_from
        date_to = self.date_to

        # No date_to set so far: automatically compute one 8 hours later
        if date_from and not date_to:
            date_to_with_delta = fields.Datetime.from_string(
                date_from) + timedelta(hours=HOURS_PER_DAY)
            self.date_to = str(date_to_with_delta)

        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            # QTL Modify
            # Added sudo() to call _get_number_of_days
            self.number_of_days_temp = self.sudo()._get_number_of_days(
                date_from, date_to, self.employee_id.id)
        else:
            self.number_of_days_temp = 0

    @api.onchange('date_to')
    def _onchange_date_to(self):
        """ Update the number_of_days. """
        date_from = self.date_from
        date_to = self.date_to

        # Compute and update the number of days
        if (date_to and date_from) and (date_from <= date_to):
            # QTL Modify
            # Added sudo() to call _get_number_of_days
            self.number_of_days_temp = self.sudo()._get_number_of_days(
                date_from, date_to, self.employee_id.id)
        else:
            self.number_of_days_temp = 0

    @api.multi
    def _create_resource_leave(self):
        """ This method will create entry in resource calendar leave object
        at the time of holidays validated """
        for leave in self:
            self.env['resource.calendar.leaves'].create({
                'name': leave.name,
                'date_from': leave.date_from,
                'holiday_id': leave.id,
                'date_to': leave.date_to,
                # QTL Modify
                # Add sudo() to access employee's field
                'resource_id': leave.employee_id.sudo().resource_id.id,
                'calendar_id':
                    leave.employee_id.sudo().resource_id.calendar_id.id
            })
        return True
