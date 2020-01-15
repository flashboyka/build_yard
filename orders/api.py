from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication

from orders.models import Order, OrderItem
from contragents.api import ContragentResource


class OrderItemResource(ModelResource):
    class Meta:
        queryset = OrderItem.objects.all()
        resource_name = 'orderitem'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()


class OrderResource(ModelResource):
    contragent  = fields.ForeignKey(ContragentResource, 'contragent', full=True)
    orderitem = fields.ToManyField('orders.api.OrderItemResource',
                                   'orderitem_set', full=True)

    class Meta:
        queryset = Order.objects.all()
        resource_name = 'orders'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
        excludes = ['created', 'edited']
