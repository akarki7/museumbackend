from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SitesAdminViewSet, SitesFrontendViewSet

router = DefaultRouter()
router.register(r"admin", SitesAdminViewSet , basename="admin")
router.register(r"sites", SitesFrontendViewSet, basename="sites")
urlpatterns = router.urls
