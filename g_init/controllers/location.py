import json
from odoo.http import Response, route,request,Controller

class LocationSearch(Controller):
    @route('/geometry/location/provinces', type="http", auth="none", method=['GET'],cors='*')
    def province_search(self, **kw):
        provinces = request.env['res.province'].sudo().search([]).read(['name','province_code'])
        values = { 
            "results": {
                    "parent": "None",
                    "level":"province",
                    "items": provinces
                } 
        } 
        headers = {'Content-Type': 'application/json'}
        return Response(json.dumps(values), headers=headers)
    
    
    @route('/geometry/location/provinces/<string:code>', type="http", auth="none", method=['GET'],cors='*')
    def district_search_by_province(self,code, **kw):
        province_code = code or '01'
        district = request.env['res.district'].sudo().search([('parent_code','=',province_code)]).read(['name','district_code'])
        values = { 
           "results": {
                    "parent": province_code,
                    "level":"district",
                    "items": district
                } 
        }
        headers = {'Content-Type': 'application/json'}
        return Response(json.dumps(values), headers=headers)
    
    
    

    @route('/geometry/location/districts/<string:code>', type="http", auth="none", method=['GET'],cors='*')
    def ward_search_by_district(self,code, **kw):
        district_code = code or '01'
        district = request.env['res.ward'].sudo().search([('parent_code','=',district_code)]).read(['name','ward_code'])
        values = { 
           "results": {
                    "parent": district_code,
                    "level":"ward",
                    "items": district
                } 
        }
        headers = {'Content-Type': 'application/json'}
        return Response(json.dumps(values), headers=headers)