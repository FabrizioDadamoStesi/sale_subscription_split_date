from dateutil.relativedelta import relativedelta
from datetime import datetime

from odoo import fields, models, api


def shifted_date(interval, date_type):
    delta_time = None
    if date_type == 'days':
        delta_time = relativedelta(days=interval)

    elif date_type == 'weeks':
        delta_time = relativedelta(weeks=interval)

    elif date_type == 'months':
        delta_time = relativedelta(months=interval)

    elif date_type == 'years':
        delta_time = relativedelta(years=interval)
    else:
        delta_time = relativedelta(days=interval)

    return delta_time



class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    remains_days= fields.Integer('Days to Delivery')


    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        product = res.product_id
        if product:
            if product.recurring_invoice:
                if product.subscription_line_ids:
                    for abb in product.subscription_line_ids:
                        date = res.order_id.date_order
                        delta_time = None
                        today = date
                        for i in range(abb.period or 0):
                            if delta_time is None:
                                delta_time= shifted_date(abb.every, abb.months)
                            date = date + delta_time
                            diff = date - today
                            print(diff.days)

                            res.create({
                                'name':abb.name,
                                'product_id': abb.product_id.id,
                                'order_id': res.order_id.id,
                                'product_uom_qty': abb.qty,
                                'commitment_date': date,
                                'remains_days': diff.days,
                            })
        return res









