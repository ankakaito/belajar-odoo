# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo_university(models.Model):
#     _name = 'odoo_university.odoo_university'
#     _description = 'odoo_university.odoo_university'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
