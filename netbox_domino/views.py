from netbox.views import generic

from . import filtersets, forms, models, tables


class DomainView(generic.ObjectView):
    queryset = models.Domain.objects.all()


class DomainListView(generic.ObjectListView):
    queryset = models.Domain.objects.all()
    table = tables.DomainTable
    filterset = filtersets.DomainFilterSet
    filterset_form = forms.DomainFilterForm


class DomainEditView(generic.ObjectEditView):
    queryset = models.Domain.objects.all()
    form = forms.DomainForm


class DomainDeleteView(generic.ObjectDeleteView):
    queryset = models.Domain.objects.all()


class DomainChangelogView(generic.ObjectChangeLogView):
    queryset = models.Domain.objects.all()


class DomainBulkEditView(generic.BulkEditView):
    queryset = models.Domain.objects.all()
    filterset = filtersets.DomainFilterSet
    table = tables.DomainTable
    form = forms.DomainBulkEditForm


class DomainBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Domain.objects.all()
    filterset = filtersets.DomainFilterSet
    table = tables.DomainTable


class DomainBulkImportView(generic.BulkImportView):
    queryset = models.Domain.objects.all()
    model_form = forms.DomainCSVForm
    table = tables.DomainTable
