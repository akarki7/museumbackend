from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from .serializers import SignUpSerializer, UserSerializer
from .models import User

class SignUpViewset(CreateModelMixin, GenericViewSet):
    serializer_class=SignUpSerializer
    queryset = User.objects.all()

class ListUsersViewSet(ListModelMixin, GenericViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    # permission_classes=[IsAdminUser]
# Create your views here.
