from netbox.tables import NetBoxTable, columns

from .models import Domain


class DomainTable(NetBoxTable):
    pk = columns.ToggleColumn()
    name = columns.Column(linkify=True)
    tenant = columns.Column(linkify=True)
    description = columns.MarkdownColumn(truncate_words=15)
    tags = columns.TagColumn()

    class Meta(NetBoxTable.Meta):
        model = Domain
        fields = ("pk", "name", "ip_address", "tenant", "description", "tags")
        default_columns = ("name", "ip_address", "tenant")
