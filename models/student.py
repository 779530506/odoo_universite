# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteStudent(models.Model):
    _name = 'universite.student'

    f_name = fields.Char("first name")
    l_name = fields.Char("last name")
    sexe   = fields.Selection([("male","male"),("female","female")])
    cni = fields.Char("carte ")
    address = fields.Text()
    birthday = fields.Date()
    #registration_date = fields.Datetime()
    email = fields.Char()
    phone = fields.Char()
