# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteDepartement(models.Model):
    _name = 'universite.departement'

    name = fields.Char(" name")
    code = fields.Char()
   
