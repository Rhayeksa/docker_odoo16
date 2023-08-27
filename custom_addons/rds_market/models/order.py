# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Order(models.Model):
    _name = 'rds_market.order'
    _description = 'rds market order model'

    order_code = fields.Char(
        string='order_code',
        size=45,
        required=True,
        help='Order Code',
    )

    customer_id = fields.Many2one(
        comodel_name='rds_market.customer',
        string='customer_id',
        required=True,
        help='Customer Id from model customer',
    )

    order_detail_ids = fields.One2many(
        'rds_market.product.order',
        'product_order_code',
        string='Product Order',
    )
