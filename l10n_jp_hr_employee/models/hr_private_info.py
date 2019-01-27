# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
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
        string='Company',
        store=True,
    )
    private_country_id = fields.Many2one(
        'res.country',
        string='Nationality (Private)',
        required=True,
    )
    roman_family_name = fields.Char(
        'Family Name (Roman)',
    )
    roman_given_name = fields.Char(
        'Given Name (Roman)',
    )
    birthday = fields.Date(
        'Birthday',
        required=True,
    )
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female')],
        required=True,
    )
    private_phone = fields.Char(
        'Private Phone',
        required=True,
    )
    private_email = fields.Char(
        'Private Email',
        required=True,
    )
    postal_code = fields.Char(
        'Postal Code',
        required=True,
    )
    address_pref = fields.Char(
        'Prefecture',
        placeholder="Prefecture",
    )
    address_street = fields.Char(
        'Current Address',
        required=True,
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
        [('father', 'Father'),
         ('mother', 'Mother'),
         ('child', 'Child'),
         ('grand_father', 'Grand Father'),
         ('grand_mother', 'Grand Mother'),
         ('other', 'Other')],
        'Emerg. Contact Type',
        required=True,
    )
    emerg_contact_desc = fields.Char(
        'Emerg. Contact Description',
    )
    emerg_contact_name = fields.Char(
        'Emerg. Contact Name',
        required=True,
    )
    emerg_contact_postal_code = fields.Char(
        'Emerg. Contact Postal Code',
    )
    emerg_contact_address = fields.Char(
        'Emerg. Contact Address',
    )
    emerg_contact_phone = fields.Char(
        'Emerg. Contact Phone',
        required=True,
    )
    bank_id = fields.Many2one(
        'res.bank',
        string='Bank',
        required=True,
    )
    bank_branch = fields.Char(
        'Bank Branch',
        required=True,
    )
    bank_acc_type = fields.Selection(
        [('savings', 'Savings'),
         ('current', 'Current')],
        'Account Type',
        required=True,
        default='savings',
    )
    bank_acc_number = fields.Char(
        'Account Number',
        required=True,
    )
    bank_acc_holder = fields.Char(
        'Account Holder',
        required=True,
    )
    furi_bank_acc_holder = fields.Char(
        'Account Holder Furigana',
        required=True,
    )
    school_name = fields.Char(
        'School Name',
        required=True,
    )
    school_dept_name = fields.Char(
        'Deartment/Course Name',
        required=True,
    )
    school_completion = fields.Selection(
        [('completed', 'Completed'),
         ('unfinished', 'Unfinished'),
         ('other', 'Other')],
        'School Completion',
        required=True,
    )
    school_completion_desc = fields.Char(
        'School Completion Description',
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
    pension_number = fields.Char(
        'Pension Number',
        required=True,
    )
    employment_ins_number = fields.Char(
        'Emp. Insurance Number',
        required=True,
    )
    disability_class_id = fields.Many2one(
        'hr.disability.class',
        string='Disability Class',
    )
    widowhood = fields.Selection(
        [('widow', 'Widow'),
         ('special', 'Special Widow'),
         ('widower', 'Widower')],
    )
    working_student_deduction = fields.Boolean(
        'Working Student Deduction',
    )
    note = fields.Text()
    visa_number = fields.Char(
        'Visa Number',
    )
    date_visa_expiry = fields.Date(
        'Visa Expiry Date',
    )
    work_permit_number = fields.Char(
        'Work Permit Number',
    )
    residence_card = fields.Binary(
        'Residence Card',
    )
    residence_card_filename = fields.Char(
        'Residence Card File Name',
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('confirmed', 'Confirmed'),
    ], string='Status', track_visibility='onchange', default='draft')

    _sql_constraints = [
        ('employee_id_uniq', 'unique (employee_id, company_id)',
         'Only one record is allowed per employee per company.')]

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
            self.roman_family_name = self.roman_family_name.upper()

    @api.onchange('roman_given_name')
    def _onchange_roman_given_name(self):
        if self.roman_given_name:
            self.roman_given_name = self.roman_given_name.upper()

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

    @api.onchange('bank_acc_holder')
    def _onchange_bank_acc_holder(self):
        if self.bank_acc_holder:
            self.bank_acc_holder = jaconv.h2z(
                self.bank_acc_holder, ascii=True, digit=True)

    @api.onchange('furi_bank_acc_holder')
    def _onchange_furi_bank_acc_holder(self):
        if self.furi_bank_acc_holder:
            # no space allowd inside the string
            self.furi_bank_acc_holder = "".join(jaconv.z2h(
                jaconv.hira2kata(self.furi_bank_acc_holder)).split())

    @api.constrains('private_phone', 'emerg_contact_phone', 'postal_code',
                    'emerg_contact_postal_code', 'bank_acc_number')
    def _check_digit_fields(self):
        for rec in self:
            msg = _("Only digits are allowed for %s field.")
            if rec.private_phone and not rec.private_phone.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % ("Private Phone"))
            if rec.emerg_contact_phone and not rec.emerg_contact_phone.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % ("Emerg. Contact Phone"))
            if rec.postal_code and not rec.postal_code.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % ("Postal Code"))
            if rec.emerg_contact_postal_code and not \
                    rec.emerg_contact_postal_code.encode('utf-8').isdigit():
                raise ValidationError(msg % ("Emerg. Contact Postal Code"))
            if rec.bank_acc_number and not rec.bank_acc_number.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % ("Account Number"))

    @api.constrains('postal_code', 'emerg_contact_postal_code',
                    'bank_acc_number')
    def _check_digits(self):
        for rec in self:
            msg = _("%s should be %s digit(s).")
            if rec.postal_code and not len(rec.postal_code) == 7:
                raise ValidationError(msg % ("Postal Code", "7"))
            if rec.emerg_contact_postal_code and not len(
                    rec.emerg_contact_postal_code) == 7:
                raise ValidationError(msg % (
                    "Emerg. Contact Postal Code", "7"))
            if rec.bank_acc_number and not len(rec.bank_acc_number) == 7:
                raise ValidationError(msg % ("Account Number", "7"))

    @api.constrains('private_email')
    def _check_email(self):
        for rec in self:
            msg = _("%s seems to be incorrect.")
            if rec.private_email and not re.match(
                    # ref: https://www.w3.org/TR/html5/forms.html#valid-e-mail-address
                    r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
                    rec.private_email):
                raise ValidationError(msg % ("Private Email"))
