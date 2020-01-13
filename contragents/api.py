from tastypie.resources import ModelResource

from contragents.models import Contragent


class ContragentResource(ModelResource):
    class Meta:
        queryset = Contragent.objects.all()
        resource_name = 'contragents'
