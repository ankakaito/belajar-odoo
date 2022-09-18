# -*- coding: utf-8 -*-
# from odoo import http


# class CourseAcademy(http.Controller):
#     @http.route('/course_academy/course_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/course_academy/course_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('course_academy.listing', {
#             'root': '/course_academy/course_academy',
#             'objects': http.request.env['course_academy.course_academy'].search([]),
#         })

#     @http.route('/course_academy/course_academy/objects/<model("course_academy.course_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('course_academy.object', {
#             'object': obj
#         })
