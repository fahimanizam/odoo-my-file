# -*- coding: utf-8 -*-
{
    'name': "education_erp_2",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nova",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'account', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherited_account_partner.xml',
        'views/inherited_base_partner.xml',
        'views/inherited_crm_partner.xml',
        'views/inherited_sale_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
