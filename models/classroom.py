# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteClassroom(models.Model):
    _name = 'universite.classroom'

    name = fields.Char(" name")
    code = fields.Char("")
   
