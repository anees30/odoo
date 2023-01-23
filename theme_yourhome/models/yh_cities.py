from odoo import models, fields, api


class YourHomeCities(models.Model):
    _name = 'yh.cities'
    _description = 'Your Home Cities'

    country_id = fields.Many2one(comodel_name='res.country', string='Country', required=True)
    state_id = fields.Many2one(comodel_name='res.country.state', string='City/State', domain="[('country_id', '=', country_id)]")
    description = fields.Char()
    image = fields.Binary()