# -*- coding: utf-8 -*-
from odoo import models, fields


class HospitalPatient(models.Model):
    """
    Model for managing hospital patients.
    Stores personal details, contact info, and links to doctor / appointments.
    """
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _rec_name = 'name'

    # -------------------------------------------------------------------------
    # Basic Information
    # -------------------------------------------------------------------------
    name = fields.Char(
        string='Patient Name',
        required=True,
        help='Full name of the patient'
    )
    date_of_birth = fields.Date(
        string='Date of Birth',
        help='Patient date of birth'
    )
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        string='Gender',
        required=True,
        default='male',
        help='Biological gender of the patient'
    )
    age = fields.Integer(
        string='Age',
        help='Age of the patient in years'
    )

    # -------------------------------------------------------------------------
    # Contact Information
    # -------------------------------------------------------------------------
    phone = fields.Char(
        string='Phone',
        help='Primary contact number'
    )
    email = fields.Char(
        string='Email',
        help='Email address of the patient'
    )

    # -------------------------------------------------------------------------
    # Relational Fields
    # -------------------------------------------------------------------------
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Assigned Doctor',
        help='Primary doctor assigned to this patient'
    )
    appointment_ids = fields.One2many(
        comodel_name='hospital.appointment',
        inverse_name='patient_id',
        string='Appointments',
        help='All appointments linked to this patient'
    )

    # -------------------------------------------------------------------------
    # System / Utility
    # -------------------------------------------------------------------------
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Uncheck to archive the patient record (soft delete)'
    )
