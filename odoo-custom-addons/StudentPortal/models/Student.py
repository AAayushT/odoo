from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta

class Student(models.Model):
    _name = "student"
    _description = "Brief student details are here"

    id = fields.Integer(required = True)
    name = fields.Char(string='Name', required=True)
    dob = fields.Date(required=True)
    doj = fields.Date(required=True)
    age = fields.Integer(compute='_cal_age')
    year = fields.Char(compute='_cal_year')
    batch = fields.Many2one("batch", string="Batch", required=True)
    roll_number = fields.Char()
    image = fields.Binary(string="Student Image")
    _sql_constraints = [
        ('uniq_roll_number', 'unique(roll_number)', "A name already exists with this roll-no . Roll-no. must be unique!"),
    ]

    @api.depends('dob')
    def _cal_age(self):
        for record in self:
            if record.dob:
                today = date.today()
                record.age = today.year - record.dob.year - ((today.month, today.day) < (record.dob.month, record.dob.day))
            else:
                record.age = 0
            

    @api.depends('doj')
    def _cal_year(self):
        for record in self:
            years = relativedelta(date.today(), record.doj).years
            if years < 1:
                record.year="1"
            elif years < 2:
                record.year="2"
            elif years < 3:
                record.year="3"
            elif years < 4:
                record.year="4"
            else:
                record.year="passed out"

