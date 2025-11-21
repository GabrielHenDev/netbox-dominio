from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from . import serializers


class DomainViewSet(NetBoxModelViewSet):
    queryset = models.Domain.objects.all()
    serializer_class = serializers.DomainSerializer
    filterset_class = filtersets.DomainFilterSet
