from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication

from goods.models import Good


class GoodResource(ModelResource):
    class Meta:
        queryset = Good.objects.all()
        resource_name = 'goods'
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
