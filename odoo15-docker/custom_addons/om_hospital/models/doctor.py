# -*- coding: utf-8 -*-
from odoo import models, fields


class HospitalDoctor(models.Model):
    """
    Model for managing hospital doctors.
    Stores professional details and contact information.
    """
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    _rec_name = 'name'

    # -------------------------------------------------------------------------
    # Basic Information
    # -------------------------------------------------------------------------
    name = fields.Char(
        string='Doctor Name',
        required=True,
        help='Full name of the doctor'
    )
    specialization = fields.Char(
        string='Specialization',
        help='Area of medical expertise (e.g. Cardiology, Pediatrics)'
    )

    # -------------------------------------------------------------------------
    # Contact Information
    # -------------------------------------------------------------------------
    phone = fields.Char(
        string='Phone',
        help='Primary contact number of the doctor'
    )

    # -------------------------------------------------------------------------
    # System / Utility
    # -------------------------------------------------------------------------
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Uncheck to archive the doctor record (soft delete)'
    )
