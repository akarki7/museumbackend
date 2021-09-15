from django.shortcuts import render
from django.views.static import serve
from django.conf import settings
from django.http import HttpResponseBadRequest

# Create your views here.

def authenticate_and_serve(request, path):
    if request.user.is_authenticated:
        return serve(request, path, settings.MEDIA_ROOT)
    else:
        return HttpResponseBadRequest("Selected resource not found")
