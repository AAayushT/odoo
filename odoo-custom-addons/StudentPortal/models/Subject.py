from odoo import fields, models

class Subject(models.Model):
    _name="subject"
    _description="The subjects available for different branches"

    id = fields.Integer(required = True)
    name = fields.Char(required=True)
    branch_id = fields.Many2one("branch", string="Branch", required=True)
    teacher_id = fields.Many2one("teacher", string="Teacher", required=True)
