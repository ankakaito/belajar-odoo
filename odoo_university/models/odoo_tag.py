from odoo import  fields, models

class OdooTag(models.Model):
    _name = 'odoo.tag' # membuat Field


    name = fields.Char('Name')