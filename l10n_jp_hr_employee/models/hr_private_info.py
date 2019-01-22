# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HrPrivateInfo(models.Model):
    _name = 'hr.private.info'
    _rec_name = 'employee_id'

    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
    )
    name_furigana = fields.Char(
        related='employee_id.name_furigana',
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
    roman_spelling = fields.Char(
        'Roman Spelling',
        required=True,
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
    current_address = fields.Char(
        'Current Address',
        required=True,
    )
    address_furigana = fields.Char(
        'Address Furigana',
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
    emerg_contact_sns = fields.Char(
        'Emerg. Contact SNS',
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
    )
    bank_acc_number = fields.Char(
        'Account Number',
        required=True,
    )
    bank_acc_holder = fields.Char(
        'Account Holder',
        required=True,
    )
    bank_acc_holder_furigana = fields.Char(
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
    terminal_education = fields.Selection(
        [('doctorate', 'Doctorate'),
         ('master', 'Master'),
         ('undergrad', 'Undergraduate'),
         ('associate', 'Associate'),
         ('highschool', 'High School')],
        'Terminal Education',
        required=True,
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
    pension_book = fields.Binary(
        string='Pension Book',
    )
    pension_book_filename = fields.Char(
        string='Pension Book File Name',
    )
    pension_number_unsure = fields.Boolean(
        'Unsure about Pension Number',
    )
    employment_ins_number = fields.Char(
        'Emp. Insurance Number',
        required=True,
    )
    employment_ins_number_unsure = fields.Boolean(
        'Unsure about Emp. Insurance Number',
    )
    previous_employer = fields.Char(
        'Previous Employer',
    )
    previous_emp_from = fields.Date(
        'Prev. Emp. Start',
    )
    previous_emp_to = fields.Date(
        'Prev. Emp. Finish',
    )
    employment_ins_card = fields.Binary(
        'Emp. Insurance Card',
    )
    employment_ins_card_filename = fields.Char(
        'Emp. Insurance Card File Name',
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

    @api.constrains('private_phone')
    def _check_private_phone(self):
        for rec in self:
            if rec.private_phone and not rec.private_phone.encode(
                    'utf-8').isdigit():
                raise ValidationError(_("Only digits are allowed for the "
                                        "Private Phone field."))

    @api.constrains('postal_code')
    def _check_postal_code(self):
        for rec in self:
            if rec.postal_code:
                if not rec.postal_code.encode('utf-8').isdigit():
                    raise ValidationError(_("Only digits are allowed for the "
                                            "Postal Code field."))
                if not len(rec.postal_code) == 7:
                    raise ValidationError(_("Postal Code should be 7 digits."))
