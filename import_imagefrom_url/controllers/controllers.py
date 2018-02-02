# -*- coding: utf-8 -*-
from odoo import http

# class ImportImagefromUrl(http.Controller):
#     @http.route('/import_imagefrom_url/import_imagefrom_url/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/import_imagefrom_url/import_imagefrom_url/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('import_imagefrom_url.listing', {
#             'root': '/import_imagefrom_url/import_imagefrom_url',
#             'objects': http.request.env['import_imagefrom_url.import_imagefrom_url'].search([]),
#         })

#     @http.route('/import_imagefrom_url/import_imagefrom_url/objects/<model("import_imagefrom_url.import_imagefrom_url"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('import_imagefrom_url.object', {
#             'object': obj
#         })