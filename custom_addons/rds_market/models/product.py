# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Product(models.Model):
    _name = 'rds_market.product'
    _description = 'rds market product model'

    name = fields.Char(
        string='name',
        size=255,
        required=True,
        help='Product Name',
    )

    price = fields.Integer(
        string='price',
        required=True,
        help='Product Price'
    )

    description = fields.Text(
        string='description',
        required=True,
        help='Product Description'
    )
