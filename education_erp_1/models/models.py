# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CustomStudent(models.Model):
    _inherit = 'op.student'

    board_roll_number = fields.Char('Board Roll Number')
    roll_number = fields.Char('Roll Number')
    registration_number = fields.Char('Registration Number')
    active = fields.Boolean(default=True)

class CustomFaculty(models.Model):
    _inherit = 'op.faculty'

    department = fields.Many2one('op.department', 'Academic Department')

# class CustomStudentMigrate(models.Model):
#     _inherit = "student.migrate"
#
#     department_from_id = fields.Many2one('op.department', 'From Department')
#     department_to_id = fields.Many2one('op.department', 'To Department')


