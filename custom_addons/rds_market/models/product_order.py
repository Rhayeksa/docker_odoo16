# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OrderDetail(models.Model):
    _name = 'rds_market.order.detail'
    _description = 'rds market order detail model'

    product_order_code = fields.Char(
        string='product_order_code',
        size=45,
        required=True,
        help='Order Code',
    )

    quantity = fields.Integer(
        string='quantity',
        required=True,
        help='Order Quantity',
    )

    product_id = fields.Many2one(
        'rds_market.product',
        string='product',
    )
