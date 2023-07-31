from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Model for storing Student Details!'

    name = fields.Char(string = "Student Name")
    age = fields.Integer(string = "Age")
    classs = fields.Char(string = "Class")
