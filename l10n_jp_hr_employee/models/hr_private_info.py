# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


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
    private_country_id = fields.Many2one(
        'res.country',
        string='Nationality (Private)',
    )
    roman_spelling = fields.Char(
        'Roman Spelling',
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
    current_address = fields.Char(
        'Current Address',
    )
    address_furigana = fields.Char(
        'Address Furigana',
    )
    residence_cert = fields.Many2many(
        'ir.attachment',
        string='Residence Certificate',
    )
    emerg_contact_type = fields.Selection(
        [('father', 'Father'),
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
    emerg_contact_sns = fields.Char(
        'Emerg. Contact SNS',
    )
    bank_id = fields.Many2one(
        'res.bank',
        string='Bank',
    )
    bank_branch = fields.Char(
        'Bank Branch',
    )
    bank_acc_type = fields.Selection(
        [('savings', 'Savings'),
         ('current', 'Current')],
        'Account Type',
    )
    bank_acc_number = fields.Char(
        'Account Number',
    )
    bank_acc_holder = fields.Char(
        'Account Holder',
    )
    bank_acc_holder_furigana = fields.Char(
        'Account Holder Furigana',
    )
    school_name = fields.Char(
        'School Name',
    )
    school_dept_name = fields.Char(
        'Deartment/Course Name',
    )
    terminal_education = fields.Selection(
        [('doctorate', 'Doctorate'),
         ('master', 'Master'),
         ('undergrad', 'Undergraduate'),
         ('associate', 'Associate'),
         ('highschool', 'High School')],
        'Terminal Education',
    )
    qualification_ids = fields.One2many(
        'hr.qualification',
        'private_info_id',
        string='Qualification',
    )
