# -*- coding: utf-8 -*-
# from odoo import http


# class ReportCustomization(http.Controller):
#     @http.route('/report_customization/report_customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_customization/report_customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_customization.listing', {
#             'root': '/report_customization/report_customization',
#             'objects': http.request.env['report_customization.report_customization'].search([]),
#         })

#     @http.route('/report_customization/report_customization/objects/<model("report_customization.report_customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_customization.object', {
#             'object': obj
#         })
