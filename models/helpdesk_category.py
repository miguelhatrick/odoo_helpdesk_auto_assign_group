# Copyright (C)
# Copyright 2021- Miguel Hatrick(<http://www.dacosys.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class HelpdeskCategory(models.Model):
    """Helpdesk Ticket Category addon."""
    _inherit = "helpdesk.ticket.category"

    team_id = fields.Many2one(
        'helpdesk.ticket.team',
        string="Automatic team",
        default=False
    )

    default_user_id = fields.Many2one(
        'res.users',
        string="Automatic assigned user",
        default=False
    )
