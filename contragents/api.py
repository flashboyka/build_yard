from tastypie.resources import ModelResource
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import BasicAuthentication
from contragents.models import Contragent


class ContragentResource(ModelResource):
    class Meta:
        queryset = Contragent.objects.all()
        resource_name = 'contragents'
        #authorization = Authorization()
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
