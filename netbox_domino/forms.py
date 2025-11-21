from django import forms
from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelForm,
    NetBoxModelImportForm,
)
from tenancy.models import Tenant
from utilities.forms.fields import (
    CSVModelChoiceField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    TagField,
)

from .models import Domain


class DomainForm(NetBoxModelForm):
    tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), required=False)
    tags = TagField(required=False)

    class Meta:
        model = Domain
        fields = ("name", "ip_address", "tenant", "description", "tags")


class DomainBulkEditForm(NetBoxModelBulkEditForm):
    tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), required=False)
    ip_address = forms.GenericIPAddressField(required=False)
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
    )

    model = Domain
    nullable_fields = ("tenant", "ip_address", "description")
    fieldsets = (
        ("Domínio", ("tenant", "ip_address", "description")),
    )


class DomainCSVForm(NetBoxModelImportForm):
    tenant = CSVModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name="slug",
        required=False,
        help_text="Slug do tenant (ex.: corporativo)",
    )

    class Meta:
        model = Domain
        fields = ("name", "ip_address", "tenant", "description")


class DomainFilterForm(NetBoxModelFilterSetForm):
    model = Domain
    q = forms.CharField(
        required=False,
        label="Busca",
    )
    tenant_id = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        label="Tenant (ID)",
    )
    tenant = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        to_field_name="slug",
        label="Tenant (slug)",
    )
    tag = TagField(required=False)
