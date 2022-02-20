from odoo import fields, models

class Teacher(models.Model):
    _name = "teacher"
    _description = "Edit and View various details of the teachers including the subjects they take etc."

    id = fields.Integer(required=True)
    name = fields.Char(required=True)
    employee_id = fields.Char(required=True)
    subject_list = fields.One2many("subject", "teacher_id", string="Subject list") 
    _sql_constraints = [
        ('uniq_employee_id', 'unique(employee_id)', "A name already exists with this employee-id . employee-id. must be unique!"),
    ]
