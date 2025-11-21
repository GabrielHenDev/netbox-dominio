from netbox.api.routers import NetBoxRouter

from . import viewsets

app_name = "netbox_domino"

router = NetBoxRouter()
router.register("domains", viewsets.DomainViewSet)

urlpatterns = router.urls
