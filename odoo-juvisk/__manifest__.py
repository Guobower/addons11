# -*- coding: utf-8 -*-
{
    'name': "Prasetia Juvisk Sinergy",

    'summary': """
        Battery System Rent Module""",

    'description': """
        Battery System Rent Module
    """,

    'author': "easierware",
    'website': "http://www.easiere.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account',
                'project', 'sale',
                'purchase',
                # 'purchase_requisition',
                'work_order'],

    # always loaded ,del company
    'data': [
        'report/purchase_report.xml',
        # 'report/purchase_request_report.xml',
        # 'report/invoice_report.xml',
        # 'report/account_move.xml',
        # 'view/invoice.xml',
        'data/juvisk_data.xml'
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}