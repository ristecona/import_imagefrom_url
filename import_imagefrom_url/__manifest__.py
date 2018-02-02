# -*- coding: utf-8 -*-
{
    'name': "import_imagefrom_url",

    'summary': """
        Just edit or create a product with image url and it will be automatically set on the image of the product!""",

    'description': """
        Just edit or create a product with image url and it will be automatically set on the image of the product!
    """,

    'author': "Unknown",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'price': 49,
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}