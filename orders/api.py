from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication

from orders.models import Order


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'orders'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
