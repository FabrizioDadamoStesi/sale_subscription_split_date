from odoo import models, fields,api

class ProductTemplate(models.Model):
    _inherit = 'product.template'



    #linea codice per richiamare le linee di ordine nel tab Delivery Note
    subscription_line_ids = fields.One2many('delivery.id.lines', 'delivery_id', string='Products Lines')

    # nuova riga aggiunta
    @api.onchange("recurring_invoice")
    def _onchange_recurring_invoice(self):
        for prod in self:
            prod.subscription_line_ids = False