import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from utilities.filters import TagFilter

from .models import Domain


class DomainFilterSet(NetBoxModelFilterSet):
    search_fields = ("name", "ip_address", "description")

    tenant_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name="tenant_id",
        label="Tenant (ID)",
    )
    tenant = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name="tenant__slug",
        to_field_name="slug",
        label="Tenant (slug)",
    )
    tag = TagFilter()

    class Meta:
        model = Domain
        fields = ("id", "name", "ip_address", "tenant", "tenant_id", "description")
