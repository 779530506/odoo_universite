# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversiteSubject(models.Model):
    _name = 'universite.subject'

    name = fields.Char()
    code = fields.Char()
   
