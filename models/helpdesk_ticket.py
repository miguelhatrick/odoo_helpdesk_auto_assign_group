# Copyright (C)
# Copyright 2021- Miguel Hatrick(<http://www.dacosys.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class HelpdeskItemCustom(models.Model):
    """Helpdesk Ticket addon."""
    _inherit = "helpdesk.ticket"

    @api.model
    def create(self, values):

        if values.get("category_id"):

            _category = self.env['helpdesk.ticket.category'].sudo().search([('id', '=', values.get("category_id"))])

            if _category:
                values['team_id'] = _category.team_id.id
                if values.get("user_id") is False or values.get("user_id") is None:
                    values['user_id'] = _category.default_user_id.id

        result = super(HelpdeskItemCustom, self).create(values)
        return result
