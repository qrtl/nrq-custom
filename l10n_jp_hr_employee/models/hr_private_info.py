# -*- coding: utf-8 -*-
# Copyright 2019-2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import re
from datetime import datetime

import jaconv

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


def get_years():
    year_list = []
    for i in range(1960, datetime.today().year + 1):
        year_list.append((i, str(i)))
    return year_list


class HrPrivateInfo(models.Model):
    _name = 'hr.private.info'
    _rec_name = 'employee_id'
    _inherit = ['mail.thread']
    _order = 'code, employee_id'

    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
    )
    active = fields.Boolean(
        track_visibility='onchange',
        related='employee_id.active',
        store=True,
        readonly=True,
    )
    temp_save = fields.Boolean(
        'Temporary Save',
    )
    family_name = fields.Char(
        related='employee_id.family_name',
        store=True,
    )
    given_name = fields.Char(
        related='employee_id.given_name',
        store=True,
    )
    furi_family_name = fields.Char(
        related='employee_id.furi_family_name',
        store=True,
    )
    furi_given_name = fields.Char(
        related='employee_id.furi_given_name',
        store=True,
    )
    code = fields.Char(
        related='employee_id.code',
        store=True,
        readonly=True,
    )
    company_id = fields.Many2one(
        'res.company',
        related='employee_id.company_id',
        store=True,
        readonly=True,
    )
    private_country_id = fields.Many2one(
        'res.country',
        string='Nationality (Private)',
    )
    private_country_code = fields.Char(
        related='private_country_id.code',
    )
    roman_family_name = fields.Char(
        'Family Name (Roman)',
    )
    roman_given_name = fields.Char(
        'Given Name (Roman)',
    )
    birthday = fields.Date(
        'Birthday',
    )
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female')],
    )
    private_phone = fields.Char(
        'Private Phone',
    )
    private_email = fields.Char(
        'Private Email',
    )
    postal_code = fields.Char(
        'Postal Code',
    )
    address_pref = fields.Char(
        'Prefecture',
        placeholder="Prefecture",
    )
    address_street = fields.Char(
        'Current Address',
    )
    building = fields.Char(
        'Apartment/Building',
    )
    furi_address = fields.Char(
        'Address Furigana',
    )
    furi_building = fields.Char(
        'Apartment/Building Furigana',
    )
    # we will not use ir.attachment to store PDF for security reason
    residence_cert = fields.Binary(
        string='Residence Certificate',
    )
    residence_cert_filename = fields.Char(
        string='Residence Cert File Name',
    )
    emerg_contact_type = fields.Selection(
        [('spouse', 'Spouse'),
         ('father', 'Father'),
         ('mother', 'Mother'),
         ('child', 'Child'),
         ('grand_father', 'Grand Father'),
         ('grand_mother', 'Grand Mother'),
         ('other', 'Other')],
        'Emerg. Contact Type',
    )
    emerg_contact_desc = fields.Char(
        'Emerg. Contact Description',
    )
    emerg_contact_name = fields.Char(
        'Emerg. Contact Name',
    )
    emerg_contact_postal_code = fields.Char(
        'Emerg. Contact Postal Code',
    )
    emerg_contact_address = fields.Char(
        'Emerg. Contact Address',
    )
    emerg_contact_phone = fields.Char(
        'Emerg. Contact Phone',
    )
    bank_name = fields.Char(
        'Bank Name',
    )
    bank_branch = fields.Char(
        'Bank Branch',
    )
    bank_acc_type = fields.Selection(
        [('savings', 'Savings'),
         ('current', 'Current')],
        'Bank Account Type',
        default='savings',
    )
    bank_acc_number = fields.Char(
        'Account Number',
        help='For Japan Post Bank, please remove the \'1\' in the end '
             'of the account number',
    )
    furi_bank_acc_holder = fields.Char(
        'Account Holder Furigana',
    )
    school_name = fields.Char(
        'School Name',
    )
    school_dept_name = fields.Char(
        'Deartment/Course Name',
    )
    school_completion = fields.Selection(
        [('completed', 'Completed'),
         ('unfinished', 'Unfinished'),
         ('other', 'Other')],
        'School Completion',
    )
    school_completion_desc = fields.Char(
        'Note (School Completion)',
    )
    year_left_school = fields.Selection(
        get_years(),
        'Year of Leaving School',
    )
    qualification_ids = fields.One2many(
        'hr.qualification',
        'private_info_id',
        string='Qualification',
    )
    dependant_ids = fields.One2many(
        'hr.dependant',
        'private_info_id',
        string='Dependants',
    )
    pension_code = fields.Char(
        'Pension Number Code',
        help="Please input '0000-000000' in case you are not sure about the "
             "number.",
    )
    pension_seq = fields.Char(
        'Pension Number Sequence',
    )
    pension_number = fields.Char(
        'Pension Number',
        compute='_compute_pension_number',
        store=True,
    )
    emp_ins_number_1st = fields.Char(
        'Emp. Ins. Number (1st part)',
        help="Please input '0000-000000-0' in case you are not sure about the "
             "number.",
    )
    emp_ins_number_2nd = fields.Char(
        'Emp. Ins. Number (2nd part)',
    )
    emp_ins_number_3rd = fields.Char(
        'Emp. Ins. Number (3rd part)',
    )
    emp_ins_number = fields.Char(
        'Emp. Insurance Number',
        compute='_compute_emp_ins_number',
        store=True,
    )
    note = fields.Text()
    visa_number = fields.Char(
        'Visa Number',
    )
    date_visa_expiry = fields.Date(
        'Visa Expiry Date',
    )
    residence_card = fields.Binary(
        'Residence Card',
    )
    residence_card_filename = fields.Char(
        'Residence Card File Name',
    )
    resignation_date = fields.Date(
        'Resignation Date',
    )
    resignation_reason = fields.Char(
        'Resignation Reason',
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('confirm', 'Confirmed')],
        string='Status',
        track_visibility='onchange',
        default='draft'
    )

    _sql_constraints = [
        ('employee_id_uniq', 'unique (employee_id, company_id)',
         'Only one record is allowed per employee per company.')]

    def check_digits(self, field):
        msg = {}
        field = jaconv.z2h(field, ascii=True, digit=True).replace("-", "")
        if not field.isdigit():
            field = False
            msg = {
                'warning': {
                    'title': _("Error"),
                    'message': _("Only digits are allowed.")
                }
            }
        return field, msg

    def check_alphabets(self, field):
        msg = {}
        field = jaconv.z2h(field, ascii=True, digit=True).upper()
        if re.compile(r'^[a-zA-Z]+$').match(field) is None:
            field = False
            msg = {
                'warning': {
                    'title': _("Error"),
                    'message': _("Only Roman alphabets are allowed.")
                }
            }
        return field, msg

    @api.onchange('family_name')
    def _onchange_family_name(self):
        if self.family_name:
            self.family_name = jaconv.h2z(
                self.family_name, ascii=True, digit=True)

    @api.onchange('given_name')
    def _onchange_given_name(self):
        if self.given_name:
            self.given_name = jaconv.h2z(
                self.given_name, ascii=True, digit=True)

    @api.onchange('furi_family_name')
    def _onchange_furi_family_name(self):
        if self.furi_family_name:
            self.furi_family_name = jaconv.z2h(
                jaconv.hira2kata(self.furi_family_name))

    @api.onchange('furi_given_name')
    def _onchange_furi_given_name(self):
        if self.furi_given_name:
            self.furi_given_name = jaconv.z2h(
                jaconv.hira2kata(self.furi_given_name))

    @api.onchange('roman_family_name')
    def _onchange_roman_family_name(self):
        if self.roman_family_name:
            self.roman_family_name, msg = self.check_alphabets(
                self.roman_family_name)
            if not self.roman_family_name:
                return msg

    @api.onchange('roman_given_name')
    def _onchange_roman_given_name(self):
        if self.roman_given_name:
            self.roman_given_name, msg = self.check_alphabets(
                self.roman_given_name)
            if not self.roman_given_name:
                return msg

    @api.onchange('private_phone')
    def _onchange_private_phone(self):
        if self.private_phone:
            self.private_phone, msg = self.check_digits(self.private_phone)
            if not self.private_phone:
                return msg

    @api.onchange('private_email')
    def _onchange_private_email(self):
        if self.private_email:
            self.private_email = jaconv.z2h(self.private_email, ascii=True,
                                            digit=True)

    @api.onchange('emerg_contact_phone')
    def _onchange_emerg_contact_phone(self):
        if self.emerg_contact_phone:
            self.emerg_contact_phone, msg = self.check_digits(
                self.emerg_contact_phone)
            if not self.emerg_contact_phone:
                return msg

    @api.onchange('postal_code')
    def _onchange_postal_code(self):
        if self.postal_code:
            self.postal_code, msg = self.check_digits(self.postal_code)
            if not self.postal_code:
                return msg

    @api.onchange('emerg_contact_postal_code')
    def _onchange_emerg_contact_postal_code(self):
        if self.emerg_contact_postal_code:
            self.emerg_contact_postal_code, msg = self.check_digits(
                self.emerg_contact_postal_code)
            if not self.emerg_contact_postal_code:
                return msg

    @api.onchange('address_pref')
    def _onchange_address_pref(self):
        if self.address_pref:
            self.address_pref = jaconv.h2z(
                self.address_pref, ascii=True, digit=True)

    @api.onchange('address_street')
    def _onchange_address_street(self):
        if self.address_street:
            self.address_street = jaconv.h2z(
                self.address_street, ascii=True, digit=True)

    @api.onchange('building')
    def _onchange_building(self):
        if self.building:
            self.building = jaconv.h2z(self.building, ascii=True, digit=True)

    @api.onchange('furi_address')
    def _onchange_furi_address(self):
        if self.furi_address:
            self.furi_address = jaconv.h2z(
                jaconv.hira2kata(self.furi_address), ascii=True, digit=True)

    @api.onchange('furi_building')
    def _onchange_furi_building(self):
        if self.furi_building:
            self.furi_building = jaconv.h2z(
                jaconv.hira2kata(self.furi_building), ascii=True, digit=True)

    @api.onchange('emerg_contact_name')
    def _onchange_emerg_contact_name(self):
        if self.emerg_contact_name:
            self.emerg_contact_name = jaconv.h2z(
                self.emerg_contact_name, ascii=True, digit=True)

    @api.onchange('furi_bank_acc_holder')
    def _onchange_furi_bank_acc_holder(self):
        if self.furi_bank_acc_holder:
            # no space allowd inside the string
            self.furi_bank_acc_holder = "".join(jaconv.z2h(
                jaconv.hira2kata(self.furi_bank_acc_holder)).split())

    @api.onchange('pension_code')
    def _onchange_pension_code(self):
        if self.pension_code:
            self.pension_code, msg = self.check_digits(self.pension_code)
            if not self.pension_code:
                return msg

    @api.onchange('pension_seq')
    def _onchange_pension_seq(self):
        if self.pension_seq:
            self.pension_seq, msg = self.check_digits(self.pension_seq)
            if not self.pension_seq:
                return msg

    @api.onchange('emp_ins_number_1st')
    def _onchange_emp_ins_number_1st(self):
        if self.emp_ins_number_1st:
            self.emp_ins_number_1st, msg = self.check_digits(
                self.emp_ins_number_1st)
            if not self.emp_ins_number_1st:
                return msg

    @api.onchange('emp_ins_number_2nd')
    def _onchange_emp_ins_number_2nd(self):
        if self.emp_ins_number_2nd:
            self.emp_ins_number_2nd, msg = self.check_digits(
                self.emp_ins_number_2nd)
            if not self.emp_ins_number_2nd:
                return msg

    @api.onchange('emp_ins_number_3rd')
    def _onchange_emp_ins_number_3rd(self):
        if self.emp_ins_number_3rd:
            self.emp_ins_number_3rd, msg = self.check_digits(
                self.emp_ins_number_3rd)
            if not self.emp_ins_number_3rd:
                return msg

    @api.onchange('emerg_contact_address')
    def _onchange_emerg_contact_address(self):
        if self.emerg_contact_address:
            self.emerg_contact_address = jaconv.h2z(
                self.emerg_contact_address, ascii=True, digit=True)

    @api.multi
    @api.depends('pension_code', 'pension_seq')
    def _compute_pension_number(self):
        for rec in self:
            rec.pension_number = '%s' %(rec.pension_code or '') + '-' + \
                                 '%s' %(rec.pension_seq or '')

    @api.multi
    @api.depends('emp_ins_number_1st', 'emp_ins_number_2nd',
                 'emp_ins_number_3rd')
    def _compute_emp_ins_number(self):
        for rec in self:
            rec.emp_ins_number = '%s' %(rec.emp_ins_number_1st or '') + '-' + \
                                 '%s' %(rec.emp_ins_number_2nd or '') + '-' + \
                                 '%s' %(rec.emp_ins_number_3rd or '')

    @api.constrains('private_phone', 'emerg_contact_phone', 'postal_code',
                    'emerg_contact_postal_code', 'bank_acc_number',
                    'pension_code', 'pension_seq', 'emp_ins_number_1st',
                    'emp_ins_number_2nd', 'emp_ins_number_3rd')
    def _validate_digit_fields(self):
        for rec in self:
            msg = _("Only digits are allowed for %s field.")
            if rec.private_phone and not rec.private_phone.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % _("Private Phone"))
            if rec.emerg_contact_phone and not rec.emerg_contact_phone.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % _("Emerg. Contact Phone"))
            if rec.postal_code and not rec.postal_code.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % _("Postal Code"))
            if rec.emerg_contact_postal_code and not \
                    rec.emerg_contact_postal_code.encode('utf-8').isdigit():
                raise ValidationError(msg % _("Emerg. Contact Postal Code"))
            if rec.bank_acc_number and not rec.bank_acc_number.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % _("Account Number"))
            if rec.pension_code and not \
                    rec.pension_code.encode('utf-8').isdigit() or \
                    rec.pension_seq and not \
                    rec.pension_seq.encode('utf-8').isdigit():
                raise ValidationError(msg % _("Pension Number"))
            if rec.emp_ins_number_1st and not \
                    rec.emp_ins_number_1st.encode('utf-8').isdigit() or \
                    rec.emp_ins_number_2nd and not \
                    rec.emp_ins_number_2nd.encode('utf-8').isdigit() or \
                    rec.emp_ins_number_3rd and not \
                    rec.emp_ins_number_3rd.encode('utf-8').isdigit():
                raise ValidationError(msg % _("Employment Insurance Number"))

    @api.constrains('postal_code', 'emerg_contact_postal_code',
                    'bank_acc_number', 'pension_code', 'pension_seq',
                    'emp_ins_number_1st', 'emp_ins_number_2nd',
                    'emp_ins_number_3rd')
    def _validate_digit_length(self):
        for rec in self:
            msg = _("%s should be %s digit(s).")
            if rec.postal_code and not len(rec.postal_code) == 7:
                raise ValidationError(msg % (_("Postal Code"), "7"))
            if rec.emerg_contact_postal_code and not len(
                    rec.emerg_contact_postal_code) == 7:
                raise ValidationError(msg % (_(
                    "Emerg. Contact Postal Code"), "7"))
            if rec.bank_acc_number and not len(rec.bank_acc_number) == 7:
                raise ValidationError(msg % (_("Account Number"), "7"))
            if rec.pension_code and not len(rec.pension_code) == 4:
                raise ValidationError(msg % (_(
                    "The first section of Pension Number"), "4"))
            if rec.pension_seq and not len(rec.pension_seq) == 6:
                raise ValidationError(msg % (_(
                    "The second section of Pension Number"), "6"))
            if rec.emp_ins_number_1st and not len(rec.emp_ins_number_1st) == 4:
                raise ValidationError(msg % (_(
                    "The first section of Employment Insurance Number"), "4"))
            if rec.emp_ins_number_2nd and not len(rec.emp_ins_number_2nd) == 6:
                raise ValidationError(msg % (_(
                    "The second section of Employment Insurance Number"), "6"))
            if rec.emp_ins_number_3rd and not len(rec.emp_ins_number_3rd) == 1:
                raise ValidationError(msg % (_(
                    "The third section of Employment Insurance Number"), "1"))

    @api.constrains('private_email')
    def _check_email(self):
        for rec in self:
            msg = _("%s seems to be incorrect.")
            if rec.private_email and not re.match(
                    # ref: https://www.w3.org/TR/html5/forms.html#valid-e-mail-address
                    r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
                    rec.private_email):
                raise ValidationError(msg % ("Private Email"))

    @api.multi
    def action_draft(self):
        return self.write({'state': 'draft'})

    @api.multi
    def action_submit(self):
        return self.write({'state': 'submit'})

    @api.multi
    def action_confirm(self):
        return self.write({'state': 'confirm'})

    @api.model
    def create(self, vals):
        res = super(HrPrivateInfo, self).create(vals)
        users = self.env.ref(
            'l10n_jp_hr_employee.group_employee_private_info').users
        if users:
            res.message_subscribe_users(user_ids=users.ids)
        return res

    @api.multi
    def write(self, vals):
        if 'state' in vals and vals['state'] == 'submit':
            self.send_ready_notification_email()
        return super(HrPrivateInfo, self).write(vals)

    @api.multi
    def send_ready_notification_email(self):
        self.ensure_one()
        email_act = self.action_ready_notification_email_send()
        if email_act and email_act.get('context'):
            email_ctx = email_act['context']
            self.with_context(email_ctx).message_post_with_template(
                email_ctx.get('default_template_id'))
        return True

    @api.multi
    def action_ready_notification_email_send(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference(
                'l10n_jp_hr_employee',
                'private_info_submit_notification_email')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference(
                'mail',
                'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'hr.private.info',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'user_name': self.env.user.name,
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }
