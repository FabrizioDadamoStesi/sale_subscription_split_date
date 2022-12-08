from odoo import fields, models, api
from datetime import datetime



class DeliveryIdLines(models.Model):
    _name = 'delivery.id.lines'
    _description = 'Delivery Lines'

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    company_currency_id = fields.Many2one('res.currency', related='delivery_id.currency_id')
    #linea name che mi mancava
    name = fields.Char("Name", compute="_compute_name")
    product_id = fields.Many2one('product.template', string='Product')
    delivery_id = fields.Many2one('product.template', string='Delivery ID')
    qty = fields.Integer(string='Quantity')
    list_price = fields.Float(string='Sales Price', related='product_id.list_price')

    every = fields.Integer(string='Every')
    months = fields.Selection([('days', 'Days'),
                               ('weeks', 'Weeks'),
                               ('months', 'Months'),
                               ('years', 'Years')], string='Recurrence', default='months')
    period = fields.Integer(string='Period')
    date_delivery = fields.Date(string='Date')



    #creazione di un sub totale

    price_subtotal = fields.Monetary(string='Sub Total', compute='_compute_price_subtotal',
                                     currency_field='company_currency_id')



    @api.depends('list_price', 'qty')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.list_price * rec.qty * rec.period

    @api.depends("product_id.name")
    def _compute_name(self):
        for prod in self:
            prod.name = prod.product_id.name

class SalePrices(models.Model):
    _inherit = 'product.template'


#porta a zero il valore ecomomico della subscription se questo è pari ad 1
    @api.model
    def create(self, vals):
        if vals.get('list_price') ==1:
             vals['list_price'] = 0
        res = super(SalePrices, self).create(vals)
        return res