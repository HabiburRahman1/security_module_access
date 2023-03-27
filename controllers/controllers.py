# -*- coding: utf-8 -*-
# from odoo import http


# class OdooTuitorialBackend(http.Controller):
#     @http.route('/odoo_tuitorial_backend/odoo_tuitorial_backend', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_tuitorial_backend/odoo_tuitorial_backend/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_tuitorial_backend.listing', {
#             'root': '/odoo_tuitorial_backend/odoo_tuitorial_backend',
#             'objects': http.request.env['odoo_tuitorial_backend.odoo_tuitorial_backend'].search([]),
#         })

#     @http.route('/odoo_tuitorial_backend/odoo_tuitorial_backend/objects/<model("odoo_tuitorial_backend.odoo_tuitorial_backend"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_tuitorial_backend.object', {
#             'object': obj
#         })
