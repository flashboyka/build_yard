from tastypie.resources import ModelResource

from orders.models import Order


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'orders'
