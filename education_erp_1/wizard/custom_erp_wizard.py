from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CustomStudentMigrate(models.TransientModel):
    _inherit = "student.migrate"

    department_from_id = fields.Many2one('op.department', 'From Department', required=True)
    department_to_id = fields.Many2one('op.department', 'To Department', required=True)
