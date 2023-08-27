# -*- coding: utf-8 -*-
from odoo import http

# class RdsMarket(http.Controller):
#     @http.route('/rds_market/rds_market/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rds_market/rds_market/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rds_market.listing', {
#             'root': '/rds_market/rds_market',
#             'objects': http.request.env['rds_market.rds_market'].search([]),
#         })

#     @http.route('/rds_market/rds_market/objects/<model("rds_market.rds_market"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rds_market.object', {
#             'object': obj
#         })