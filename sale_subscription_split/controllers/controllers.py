# -*- coding: utf-8 -*-
# from odoo import http


# class SalesSubscriptionDeliveryPlan(http.Controller):
#     @http.route('/sales_subscription_delivery_plan/sales_subscription_delivery_plan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_subscription_delivery_plan/sales_subscription_delivery_plan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_subscription_delivery_plan.listing', {
#             'root': '/sales_subscription_delivery_plan/sales_subscription_delivery_plan',
#             'objects': http.request.env['sales_subscription_delivery_plan.sales_subscription_delivery_plan'].search([]),
#         })

#     @http.route('/sales_subscription_delivery_plan/sales_subscription_delivery_plan/objects/<model("sales_subscription_delivery_plan.sales_subscription_delivery_plan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_subscription_delivery_plan.object', {
#             'object': obj
#         })
