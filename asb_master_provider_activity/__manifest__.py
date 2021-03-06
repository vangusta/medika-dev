# -*- coding: utf-8 -*-
{
    'name': 'Master Provider Activity',
    'version': '0.1',
    'author': 'PT Arkana Solusi Bisnis',
    'license': 'OPL-1',
    'category': 'Master',
    'website': 'http://www.arkana.co.id',
    'summary': 'Custom Master Provider Activity',
    'description': '''
        Custom master activity module for Medika
    ''',
    'depends': [
        'base', 
        'mail', 
        'portal', 
        'asb_master_provider', 
        'asb_binary_newtab', 
        'asb_master_configuration_case_activity', 
        'report_xlsx'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/master_provider_activity_views.xml',
        'wizard/export_provider_activity_views.xml',
        'report/provider_activity_xlsx_views.xml'
    ],
    'qweb': [
        'static/src/xml/button_export_template.xml',
    ],
}
