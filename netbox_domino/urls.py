from django.urls import path

from . import views

app_name = "netbox_domino"


urlpatterns = [
    path("domains/", views.DomainListView.as_view(), name="domain_list"),
    path("domains/add/", views.DomainEditView.as_view(), name="domain_add"),
    path("domains/import/", views.DomainBulkImportView.as_view(), name="domain_import"),
    path("domains/edit/", views.DomainBulkEditView.as_view(), name="domain_bulk_edit"),
    path("domains/delete/", views.DomainBulkDeleteView.as_view(), name="domain_bulk_delete"),
    path("domains/<int:pk>/", views.DomainView.as_view(), name="domain"),
    path("domains/<int:pk>/edit/", views.DomainEditView.as_view(), name="domain_edit"),
    path("domains/<int:pk>/delete/", views.DomainDeleteView.as_view(), name="domain_delete"),
    path("domains/<int:pk>/changelog/", views.DomainChangelogView.as_view(), name="domain_changelog"),
]
