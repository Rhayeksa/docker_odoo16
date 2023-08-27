# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductOrder(models.Model):
    _name = 'rds_market.product.order'
    _description = 'rds market product order model'

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
