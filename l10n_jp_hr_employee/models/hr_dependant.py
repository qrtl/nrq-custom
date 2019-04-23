# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import jaconv

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HrDependant(models.Model):
    _name = 'hr.dependant'
    _order = 'dependant_categ'

    @api.model
    def _default_currency(self):
        Currency = self.env['res.currency']
        try:
            currency_id = Currency.get_object_reference(
                'base', 'JPY')[1]
        except:
            currency_recs = Currency.search([('name', 'like', _('JPY'))])
            currency_id = currency_recs[0].id if currency_recs else False
        return currency_id

    name = fields.Char(
        string='Dependant Name',
        required=True,
    )
    furi_name = fields.Char(
        string='Dependant Name (Furi)',
        required=True,
    )
    private_info_id = fields.Many2one(
        'hr.private.info',
        string='Private Info',
    )
    employee_id = fields.Many2one(
        related='private_info_id.employee_id',
        store=True,
    )
    company_id=fields.Many2one(
        'res.company',
        related='private_info_id.company_id',
        string='Company',
        store=True,
    )
    name_furigana = fields.Char(
        'Name Furigana',
    )
    dependant_categ = fields.Selection(
        [('01_spouse', 'Spouse'),
         ('02_biological_child', 'Biological Child'),
         ('03_adopted_child', 'Adopted Child'),
         ('04_other_child', 'Other Child'),
         ('05_parent', 'Parent'),
         ('06_step_parent', 'Step Parent'),
         ('07_younger_sibling', 'Younger Sibling'),
         ('08_elder_sibling', 'Elder Sibling'),
         ('09_grand_parent', 'Grand Parent'),
         ('10_great_grand_parent', 'Great Grand Parent'),
         ('11_grand_child', 'Grand Child'),
         ('12_other', 'Other')],
        'Dependant Category',
        required=True,
    )
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female')],
        required=True,
    )
    birthday = fields.Date(
        required=True,
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
    residence_categ = fields.Selection(
        [('together', 'Living Together'),
         ('separate', 'Living Separately')],
        'Residence Category',
        required=True,
    )
    postal_code = fields.Char(
        'Postal Code',
    )
    address = fields.Char(
        'Residential Address',
    )
    furi_address = fields.Char(
        'Address Furigana',
    )
    phone = fields.Char()
    occupation = fields.Selection(
        [('unemployed', 'Unemployed'),
         ('part_time', 'Part Time Worker'),
         ('pensioner', 'Pensioner'),
         ('junior', 'Junior High or Below'),
         ('high_school', 'High School Student'),
         ('college', 'College Student'),
         ('other', 'Other')],
        'Occupation',
    )
    occupation_desc = fields.Char(
        'Occupation Description',
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=_default_currency,
    )
    income = fields.Monetary(
        help='Expected income for the coming year.',
        required=True,
    )
    amt_to_family = fields.Monetary(
        'Amount Sent to Family',
    )
    amt_to_family_confirm_doc = fields.Binary(
        'Proof of Amount Sent to Family',
        help='Please prepare a passbook copy etc. which can confirm the '
             'amount sent to family',
    )
    amt_to_family_confirm_doc_filename = fields.Char(
        string='Proof of Amount Sent to Family File Name',
    )
    disability_class = fields.Selection(
        [('normal', "Normal"),
         ('special', 'Special')],
        string='Disability Class',
    )
    disability_note = fields.Char(
        'Disability Note',
    )
    is_dependant_tax = fields.Boolean(
        'Dependant in Tax Calc.',
    )
    date_dependant_enter = fields.Date(
        'Date of Becoming a Dependant',
        help='Input the date of joining the company in case the dependant '
             'enters the dependency due to that reason ',
    )
    cause_dependant_enter = fields.Selection(
        [('1_employment', "Spouse's Employment"),
         ('2_marriage', 'Marriage'),
         ('3_left_job', 'Left Job'),
         ('4_income_decrease', 'Income Decrease'),
         ('5_other', 'Other')],
        'Cause of Becoming a Dependant',
    )
    cause_dependant_enter_note = fields.Char(
        'Cause Note',
    )
    widowhood = fields.Selection(
        [('widow', 'Widow'),
         ('special', 'Special Widow'),
         ('widower', 'Widower')],
        help="Input if applicable",
    )
    working_student_deduction = fields.Boolean(
        'Working Student Deduction',
        help="Input if applicable",
    )
    inactive = fields.Boolean(
        'Inactive',
        default=False,
    )
    inactive_date = fields.Date(
        'Inactive Date',
    )
    inactive_reason = fields.Char(
        'Inactive Reason',
    )
    appointment_letter_doc = fields.Binary(
        'Letter of Appointment',
    )
    appointment_letter_doc_filename = fields.Char(
        string='Letter of Appointment File Name',
    )
    appointment_letter_url = fields.Char(
        related='private_info_id.employee_id.company_id.appointment_letter_url',
    )


    @api.onchange('phone')
    def _onchange_phone(self):
        if self.phone:
            self.phone, msg = self.env['hr.private.info'].check_digits(
                self.phone)
            if not self.phone:
                return msg

    @api.onchange('postal_code')
    def _onchange_postal_code(self):
        if self.postal_code:
            self.postal_code, msg = self.env['hr.private.info'].check_digits(
                self.postal_code)
            if not self.postal_code:
                return msg

    @api.onchange('furi_address')
    def _onchange_furi_address(self):
        if self.furi_address:
            self.furi_address = jaconv.h2z(
                jaconv.hira2kata(self.furi_address), ascii=True, digit=True)

    @api.onchange('pension_code')
    def _onchange_pension_code(self):
        if self.pension_code:
            self.pension_code, msg = self.env['hr.private.info'].check_digits(
                self.pension_code)
            if not self.pension_code:
                return msg

    @api.onchange('pension_seq')
    def _onchange_pension_seq(self):
        if self.pension_seq:
            self.pension_seq, msg = self.env['hr.private.info'].check_digits(
                self.pension_seq)
            if not self.pension_seq:
                return msg

    @api.multi
    @api.depends('pension_code', 'pension_seq')
    def _compute_pension_number(self):
        for rec in self:
            rec.pension_number = '%s' %(rec.pension_code or '') + '-' + \
                                 '%s' %(rec.pension_seq or '')

    @api.constrains('postal_code', 'phone', 'pension_code', 'pension_seq')
    def _validate_digit_fields(self):
        for rec in self:
            msg = _("Only digits are allowed for %s field.")
            if rec.postal_code and not rec.postal_code.encode(
                    'utf-8').isdigit():
                raise ValidationError(msg % _("Postal Code"))
            if rec.phone and not rec.phone.encode('utf-8').isdigit():
                raise ValidationError(msg % _("Phone"))
            if rec.pension_code and not \
                    rec.pension_code.encode('utf-8').isdigit() or \
                    rec.pension_seq and not \
                    rec.pension_seq.encode('utf-8').isdigit():
                raise ValidationError(msg % _("Pension Number"))

    @api.constrains('postal_code', 'pension_code', 'pension_seq')
    def _validate_digit_length(self):
        for rec in self:
            msg = _("%s should be %s digit(s).")
            if rec.postal_code and not len(rec.postal_code) == 7:
                raise ValidationError(msg % (_("Postal Code"), "7"))
            if rec.pension_code and not len(rec.pension_code) == 4:
                raise ValidationError(msg % (_(
                    "The first section of Pension Number"), "4"))
            if rec.pension_seq and not len(rec.pension_seq) == 6:
                raise ValidationError(msg % (_(
                    "The second section of Pension Number"), "6"))

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.name = jaconv.h2z(self.name, ascii=True, digit=True)

    @api.onchange('furi_name')
    def _onchange_furi_name(self):
        if self.furi_name:
            self.furi_name = jaconv.z2h(jaconv.hira2kata(self.furi_name))
