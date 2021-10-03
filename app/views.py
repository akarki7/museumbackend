from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthView(APIView):
    def get(self, request, format=None):
        data = {"status": "running"}
        return Response(data)
