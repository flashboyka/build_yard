from tastypie.resources import ModelResource
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from goods.models import Good


class GoodResource(ModelResource):
    class Meta:
        queryset = Good.objects.all()
        resource_name = 'goods'
        #authorization = Authorization()
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
