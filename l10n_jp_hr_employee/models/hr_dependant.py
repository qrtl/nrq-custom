# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


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
    birthday = fields.Date()
    residence_categ = fields.Selection(
        [('together', 'Together'),
         ('apart', 'Apart')],
        'Residence Category',
    )
    postal_code = fields.Char(
        'Postal Code',
    )
    address = fields.Char(
        'Address',
    )
    address_furigana = fields.Char(
        'Address Furigana',
    )
    phone = fields.Char()
    occupation = fields.Char()
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=_default_currency,
    )
    income = fields.Monetary(
        help='Expected income for the coming year.',
    )
    earnings = fields.Monetary()
    amt_to_family = fields.Monetary(
        'Amount Sent to Family',
    )
    disability_class_id = fields.Many2one(
        'hr.disability.class',
        string='Disability Class',
    )
