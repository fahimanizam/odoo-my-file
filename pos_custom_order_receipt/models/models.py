# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


# Custom Product Template
class ProductTemplate(models.Model):
    _inherit = "product.template"

    warranty = fields.Boolean('Has warranty of  ', default=False)
    year_type = fields.Char('Warranty Limit')