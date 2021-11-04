from os import error
from django.shortcuts import render
from django.views.static import serve
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AuthenticateAndServe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, path):
        return serve(request, path, settings.MEDIA_ROOT)
