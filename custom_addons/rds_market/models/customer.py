# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Customer(models.Model):
    _name = 'rds_market.customer'
    _description = 'rds market customer model'

    name = fields.Char(
        string='name',
        size=45,
        required=True,
        help='Customer Name',
    )

    phone = fields.Char(
        string='phone',
        size=45,
        default='0',
        required=True,
        help='Customer Phone',
    )

    address = fields.Char(
        string='address',
        size=255,
        default='Home',
        required=True,
        help='Customer Address'
    )
