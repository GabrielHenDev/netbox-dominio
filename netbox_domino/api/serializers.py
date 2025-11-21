from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from rest_framework import serializers
from tenancy.api.serializers import NestedTenantSerializer

from ..models import Domain


class NestedDomainSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_domino-api:domain-detail"
    )

    class Meta:
        model = Domain
        fields = ("id", "url", "display", "name")


class DomainSerializer(NetBoxModelSerializer):
    tenant = NestedTenantSerializer(required=False, allow_null=True)

    class Meta:
        model = Domain
        fields = (
            "id",
            "url",
            "display",
            "name",
            "ip_address",
            "description",
            "tenant",
            "tags",
            "created",
            "last_updated",
        )
