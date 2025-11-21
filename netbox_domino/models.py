from django.db import models
from django.urls import reverse
from extras.models import TaggedItem
from net.fields import IPAddressField
from netbox.models import NetBoxModel
from taggit.managers import TaggableManager
from tenancy.models import Tenant


class Domain(NetBoxModel):
    name = models.CharField(max_length=255, unique=True)
    ip_address = IPAddressField(blank=True, null=True)
    description = models.TextField(blank=True)
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.PROTECT,
        related_name="domains",
        blank=True,
        null=True,
    )
    tags = TaggableManager(through=TaggedItem, blank=True)

    clone_fields = ("name", "ip_address", "tenant", "description", "tags")

    class Meta:
        ordering = ("name",)
        verbose_name = "Domínio"
        verbose_name_plural = "Domínios"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_domino:domain", args=[self.pk])
