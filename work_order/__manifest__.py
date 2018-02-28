# -*- coding: utf-8 -*-
{
    'name': "work_order",

    'summary': """
        Module work_order

        """,

    'description': """
        Surat Perintah Kerja (Indonesia)
    """,

    'author': "Prasetia",
    'website': "http://www.prasetia.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/purchase_view.xml',
        'report/work_order_report.xml',
        'report/work_order_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}