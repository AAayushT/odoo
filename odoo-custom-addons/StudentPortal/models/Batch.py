from odoo import fields, models

class Batch(models.Model):
    _name="batch"
    _description="Contains the information about for which duration he is a part of the institute"

    id = fields.Integer()
    duration = fields.Char()
    branch_id = fields.Many2one("branch", string="Branch", required=True)
