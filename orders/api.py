from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication

from orders.models import Order, OrderItem
from contragents.api import ContragentResource
from goods.api import GoodResource
from orders.models import Order


class OrderResource(ModelResource):
    contragent = fields.ForeignKey(ContragentResource, 'contragent', full=True)
    orderitem = fields.ToManyField('orders.api.OrderItemResource',
                                   'orderitem_set', null=True, full=True)
    price = fields.CharField('price')

    class Meta:
        queryset = Order.objects.all()
        resource_name = 'orders'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
        excludes = ['created', 'edited']


class OrderItemResource(ModelResource):
    order = fields.ForeignKey(OrderResource, 'order')
    good = fields.ForeignKey(GoodResource, 'good')

    class Meta:
        queryset = OrderItem.objects.all()
        resource_name = 'orderitem'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
