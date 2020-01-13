from tastypie.resources import ModelResource

from goods.models import Good


class GoodResource(ModelResource):
    class Meta:
        queryset = Good.objects.all()
        resource_name = 'goods'
