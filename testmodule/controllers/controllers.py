# -*- coding: utf-8 -*-
from odoo import http


class Testmodule(http.Controller):
    @http.route('/testmodule/testmodule',  auth='none', methods=['GET'], type='http', cors='*')
    def index(self, **kw):
        print('meo meo meo')
        abc = 'caca'
        return "Hello, world", abc

#     @http.route('/testmodule/testmodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('testmodule.listing', {
#             'root': '/testmodule/testmodule',
#             'objects': http.request.env['testmodule.testmodule'].search([]),
#         })

#     @http.route('/testmodule/testmodule/objects/<model("testmodule.testmodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testmodule.object', {
#             'object': obj
#         })
