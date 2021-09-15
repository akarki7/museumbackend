"""museum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from sites import urls as museum_urls
from django.views.static import serve
from django.conf import settings
from fileServer.views import authenticate_and_serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(museum_urls)),
    url(r"^media/(?P<path>.*)$", authenticate_and_serve),
]
