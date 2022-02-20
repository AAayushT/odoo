from odoo import fields, models

class Branch(models.Model):
    _name = "branch"
    _description = "Branches that are available with their uique ids"
    id = fields.Integer(required = True)
    name = fields.Char(required = True)
