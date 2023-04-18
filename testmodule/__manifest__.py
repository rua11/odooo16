# -*- coding: utf-8 -*-
{
    'name': "Module Test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'hr', 'board', 'g_init', 'mail','web'],
    
    'assets': {
    'web.assets_backend': [
        "/testmodule/static/src/js/popup.js",
        'testmodule/static/src/xml/video_field.xml',
        'testmodule/static/src/js/video_field.js',
        # "/testmodule/static/src/js/test_owl.js",
        # "/testmodule/static/src/js/mrp.js",
        # "/testmodule/static/src/js/code_field.js",
        # "/testmodule/static/src/xml/mrp.xml",
        # "/testmodule/static/src/js/field_widget.js",
        # "/testmodule/static/src/xml/code_field.xml",
    ],
    "web.assets_qweb": [
        # "/testmodule/static/src/xml/mrp.xml",
        # "testmodule/static/src/xml/qweb_template.xml",
        'testmodule/static/src/xml/button_tree.xml',
        
        ]
     
    },
    
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/dungdz_views.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/test_kethua_views.xml',
        'views/transient_model_views.xml',
        'views/base_model_views.xml',
        'views/test_linhtinh_view.xml',
        'views/test_mail_template.xml',
        'views/test2_mail_template.xml',
        'views/template_mail_views.xml',
        'views/menu.xml',
        
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
