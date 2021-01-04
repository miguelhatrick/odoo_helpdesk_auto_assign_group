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

        if values.get("category_id") \
                and values.get("category_id") > 0:

            _category = self.env['helpdesk.ticket.category'].search([('id', '=', values.get("category_id"))])

            values['team_id'] = _category.team_id.id
            if values['user_id'] is False:
                values['user_id'] = _category.default_user_id.id

        result = super(HelpdeskItemCustom, self).create(values)
        return result
