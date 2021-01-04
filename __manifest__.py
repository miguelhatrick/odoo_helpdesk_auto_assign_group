# -*- coding: utf-8 -*-
{
    'name': "Helpdesk auto assign team",
    # odoo_helpdesk_auto_assign_group
    'summary': """
        Assigns a Team automatically based on category""",

    'description': """
        Assigns a Team to a ticket automatically based on category
    """,

    'author': "Miguel Hatrick",
    'website': "http://www.dacosys.com",

    'category': 'Helpdesk',
    'version': '12.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk_mgmt'],

    # always loaded
    'data': [
        'views/ticket_category.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
