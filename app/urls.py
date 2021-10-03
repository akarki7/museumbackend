from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.contrib import admin
from sites import urls as museum_urls
from users import urls as auth_urls
from fileServers.views import authenticate_and_serve
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from watchman.views import status

urlpatterns = [
    path("api/health", status, name="health-view"),
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/", include(museum_urls)),
    path("auth/", include(auth_urls)),
    url(r"^media/(?P<path>.*)$", authenticate_and_serve),
]
