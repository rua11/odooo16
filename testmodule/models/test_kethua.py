from odoo import models, fields


class TestKeThua(models.Model):
    _inherit = 'sale.order'
    # _name = 'testmodule'
    _description = 'demo'

    aaaa = fields.Char(string='rac')


