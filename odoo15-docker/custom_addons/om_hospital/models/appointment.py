# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class HospitalAppointment(models.Model):
    """
    Model for managing hospital appointments.
    Includes a state machine workflow:
        Draft → In Progress → Done
                           ↓
                       Cancelled → (Reset) → Draft
    The appointment reference is auto-generated via ir.sequence.
    """
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _rec_name = 'name'

    # -------------------------------------------------------------------------
    # Reference / Identity
    # -------------------------------------------------------------------------
    name = fields.Char(
        string='Appointment Reference',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: self.env['ir.sequence'].next_by_code(
            'hospital.appointment'
        ) or 'New',
        help='Auto-generated appointment reference number'
    )

    # -------------------------------------------------------------------------
    # Core Fields
    # -------------------------------------------------------------------------
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
        required=True,
        help='Patient this appointment belongs to'
    )
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor',
        required=True,
        help='Doctor assigned to this appointment'
    )
    appointment_date = fields.Datetime(
        string='Appointment Date & Time',
        required=True,
        default=fields.Datetime.now,
        help='Scheduled date and time for the appointment'
    )
    description = fields.Text(
        string='Description / Notes',
        help='Reason for visit or additional notes'
    )

    # -------------------------------------------------------------------------
    # Workflow State
    # -------------------------------------------------------------------------
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        required=True,
        default='draft',
        tracking=True,
        help='Current state of the appointment workflow'
    )

    # -------------------------------------------------------------------------
    # System / Utility
    # -------------------------------------------------------------------------
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Uncheck to archive the appointment record (soft delete)'
    )

    # =========================================================================
    # Workflow Action Methods
    # =========================================================================

    def action_confirm(self):
        """Move appointment from Draft → In Progress."""
        for rec in self:
            if rec.state != 'draft':
                raise UserError(
                    'Only Draft appointments can be confirmed.'
                )
            rec.state = 'in_progress'

    def action_done(self):
        """Move appointment from In Progress → Done."""
        for rec in self:
            if rec.state != 'in_progress':
                raise UserError(
                    'Only In-Progress appointments can be marked as Done.'
                )
            rec.state = 'done'

    def action_cancel(self):
        """Cancel an appointment from any active state."""
        for rec in self:
            if rec.state == 'done':
                raise UserError(
                    'Completed appointments cannot be cancelled.'
                )
            rec.state = 'cancelled'

    def action_reset_draft(self):
        """Reset a Cancelled appointment back to Draft."""
        for rec in self:
            if rec.state != 'cancelled':
                raise UserError(
                    'Only Cancelled appointments can be reset to Draft.'
                )
            rec.state = 'draft'
