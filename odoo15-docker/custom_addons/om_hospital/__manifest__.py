# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management System',
    'version': '15.0.1.0.0',
    'summary': 'Manage Patients, Doctors and Appointments',
    'description': '''
        Hospital Management System
        ==========================
        A practice module for learning Odoo 15 custom development.
        Features:
            - Patient management
            - Doctor management
            - Appointment scheduling with workflow
            - PDF report for appointments
    ''',
    'category': 'Healthcare',
    'author': 'OdooMates',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        # Security — always load first
        'security/ir.model.access.csv',
        # Views
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
        'views/menu.xml',
        # Reports
        'report/appointment_report.xml',
        'report/appointment_report_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'om_hospital/static/src/css/hospital_styles.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
