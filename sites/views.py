from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from .serializers import PhotoSerializer, SiteSerializer, VideoSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from .models import Site, Photos, Videos
from .filters import SiteFilter

# Create your views here.'

class SitesViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    serializer_class = SiteSerializer
    queryset = Site.objects.all()
    filterset_class = SiteFilter

    @action(methods=["POST", "DELETE"], parser_classes=[MultiPartParser], detail=True, url_path="photos")
    def handle_photos(self, request, pk):
        if request.method == "POST":
            file = request.data.get("file", None)
            if file is None:
                raise ParseError("No file provided")
            name = request.data.get("name", None)
            photo_obj = Photos(photo=file, name=name, related_site=self.get_object())
            photo_obj.save()
            return Response({"detail": "Photo attached"}, status=status.HTTP_201_CREATED)
        else:
            photo_id = request.data.get("photo_id", None)
            if photo_id is None:
                raise ParseError("No id provided")
            try:
                photo_obj = Photos.objects.get(id=photo_id)
                photo_obj.delete()
            except Photos.DoesNotExist:
                return Response(f"Photo with id {photo_id} does not exist", status=status.HTTP_400_BAD_REQUEST)
            return Response({"detail": "Photo deleted"}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST", "DELETE"], parser_classes=[MultiPartParser], detail=True, url_path="videos")
    def handle_videos(self, request, pk):
        if request.method == "POST":
            file = request.data.get("file", None)
            if file is None:
                raise ParseError("No file provided")
            name = request.data.get("name", None)
            video_obj = Videos(video=file, name=name, related_site=self.get_object())
            video_obj.save()
            return Response({"detail": "Video attached"}, status=status.HTTP_201_CREATED)
        else:
            video_id = request.data.get("video_id", None)
            if video_id is None:
                raise ParseError("No id provided")
            try:
                video_obj = Videos.objects.get(id=video_id)
                video_obj.delete()
            except Photos.DoesNotExist:
                return Response(f"Video with id {video_id} does not exist", status=status.HTTP_400_BAD_REQUEST)
            return Response({"detail": "Video deleted"}, status=status.HTTP_204_NO_CONTENT)

class PhotosViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=PhotoSerializer
    queryset=Photos.objects.all()

class VideoViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=VideoSerializer
    queryset=Videos.objects.all()
