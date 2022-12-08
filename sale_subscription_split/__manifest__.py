# -*- coding: utf-8 -*-
{
    'name': "Sale Subscription Split",

    'summary': """
        Gestione di un Delivery Plan""",

    'description': """
        Modulo per poter frazionare in più date l'invio dei prodotti in abbonamento
    """,

    'author': "Fabrizio",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'sequence': -100,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product','sale_subscription','stock','purchase',],
    'installable': True,
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_subscription_split.xml',
        'views/quotation_subscription_split.xml',



    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
