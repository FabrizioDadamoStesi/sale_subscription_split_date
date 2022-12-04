from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'product.template'
    #_name = 'sale.order'
    #_description = 'Sale subscription lines'

    subscription_line_ids= fields.One2many('delivery.id.lines','delivery_id', string='Products Lines')

class DeliveryIdLines(models.Model):
    _name = 'delivery.id.lines'
    _description = 'Delivery Lines'
    product_id = fields.Many2one('product.product')
    date_delivery = fields.Date(string='Date')
    delivery_id = fields.Many2one('product.template', string='Delivery ID')