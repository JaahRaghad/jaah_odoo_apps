{
    'name': "Google Meet Calendar Integration",
    'version': '15.0.1.0.0',
    "category": 'Extra Tools ',
    'summary': """This module for Integrating Google Meet with the 
     Calendar.""",
    'description': """This module integrates Google Meet with the Odoo 
     calendar functionality. It allows users to create Google Meet URLs and 
     associate them with calendar events. With this integration, users can 
     easily join Google Meet meetings directly from their calendar
     events in Odoo.""",
    'author': 'jaah',
    'sequence': -1,
    'website': "https://www.jaah.it",
    'support': 'support@jaah.it',
    'company': 'jaah ERP',
    'currency': 'SR',
    'price': '1',
    'depends': ['contacts', 'calendar'],
    'data': [
        'views/res_company_views.xml',
        'views/calendar_event_views.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'license': "LGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}
