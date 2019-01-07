# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HrDependant(models.Model):
    _name = 'hr.dependant'
    _order = 'dependant_categ'

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
