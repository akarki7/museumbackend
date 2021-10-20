from rest_framework.routers import SimpleRouter
from .views import PhotosViewSet, SitesViewSet, VideoViewSet
from django.urls import path

router = SimpleRouter()
router.register(r"sites", SitesViewSet , basename="sites")
router.register(r"photos", PhotosViewSet, basename="photos")
router.register(r"videos",VideoViewSet, basename="videos")

urlpatterns = router.urls
