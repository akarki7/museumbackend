from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from .serializers import SiteSerializer
from rest_framework import status
from .models import Site

# Create your views here.

class SitesAdminViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAdminUser]
    serializer_class = SiteSerializer
    queryset = Site.objects.all()


class SitesFrontendViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SiteSerializer
    queryset = Site.objects.all()


class SignInViewSet(APIView):
    def post(request):
        username = request.data
        password = request.data
        return Response(
            data={"username": username, "password": password}, status=status.HTTP_200_OK
        )
