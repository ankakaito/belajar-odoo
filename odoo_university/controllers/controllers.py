# -*- coding: utf-8 -*-
# from odoo import http


# class OdooUniversity(http.Controller):
#     @http.route('/odoo_university/odoo_university/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_university/odoo_university/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_university.listing', {
#             'root': '/odoo_university/odoo_university',
#             'objects': http.request.env['odoo_university.odoo_university'].search([]),
#         })

#     @http.route('/odoo_university/odoo_university/objects/<model("odoo_university.odoo_university"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_university.object', {
#             'object': obj
#         })
