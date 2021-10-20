from rest_framework import serializers
from .models import Photos, Site, Videos

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photos
        exclude=["related_site"]

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Videos
        exclude=["related_site"]

class SiteSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Site
        fields = "__all__"

    
