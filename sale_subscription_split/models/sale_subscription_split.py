from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'product.template'
    product_id = fields.Many2one('product.product', string='Product')
    period = fields.Char(string='every')
    months = fields.Selection([('1month', '1 Month'), ('2months','2 Months'), ('3months', '3 Months'),('6months','6 Months'),('1year', '1 Year')],string='Cadence')
    qty = fields.Integer(string='Quantity')



    #linea codice per richiamare le linee di ordine nel tab Delivery Note
    subscription_line_ids= fields.One2many('delivery.id.lines','delivery_id', string='Products Lines')

class DeliveryIdLines(models.Model):
    _name = 'delivery.id.lines'
    _description = 'Delivery Lines'
    product_id = fields.Many2one('product.product')
    date_delivery = fields.Date(string='Date')
    delivery_id = fields.Many2one('product.template', string='Delivery ID')