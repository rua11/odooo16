# -*- coding: utf-8 -*-
import base64
from odoo import http
from odoo import api, models
from odoo.http import Response, route,request,Controller
import json
class Testmodule(Controller):
    @http.route('/testmodule/testmodule',  auth='none', methods=['GET'], type='http', cors='*')
    def index(self, **kw):
        print('meo meo meo')
        abc = 'caca'
        return "Hello, world", abc
    
    @http.route('/get_data_by_id/id', auth='none', methods=['GET'], type='http', cors='*')
    def get_data_by_id(self,**kw):
        a = request.env['dungdz'].sudo().browse(18)
        # b = json.loads(a.document_fa)
        b = a.document_fa
        c = a.video_dz
        d = base64.b64decode(a.video_dz)
        fh = open("video1.mp4", "wb")
        fh.write(base64.b64decode(d))
        fh.close()
        print(type(b))
        print(type(c))
        print(type(d))
        return d
    #get data by language
    @http.route('/get_data', auth='none', methods=['GET'], type='json', cors='*')
    def get_data_by_id(self,**kw):
        data = request.env['dungdz'].sudo().browse(31).with_context(lang='vi_VN').document_fa1
        res = {
            "data" : data
        }
        return res


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
