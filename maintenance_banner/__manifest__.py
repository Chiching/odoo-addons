# -*- coding: utf-8 -*-
{
    'name': "Maintenance Banner",
    'version': '1.0',
    'summary': """A maintenance banner""",

    'description': """
    Show a maintenance banner after navigation, you could change the banner content, background and height.
    """,

    'author': "Chiching (chnqng@qq.com)",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
    'installable': True,
    'application': True,
    'auto_install': False,
}
