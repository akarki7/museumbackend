from django.db import models
from datetime import date
from django.db.models.signals import post_delete
import os
from django.conf import settings
# Create your models here.

class TimePeriod(models.TextChoices):
    FL= "FL" ,"Flakkaserne and before"
    G1= "G1", "Grohn Barracks I"
    DP= "DP",  "DP Camp Grohn"
    G2= "G2", "Grohn Barracks II"
    RK= "RK", "Roland-Kaserne"
    JU= "JU", "IUB-JU"

class Site(models.Model):

    serial_number = models.CharField(max_length=10, null=False, primary_key=True)
    title = models.CharField(max_length=50, null=False)
    file_name = models.CharField(max_length=50, null=True, blank=True)
    preview = models.FileField(blank=True, null=True)
    # type: file, max-size: 20MB (excludign VR and AR)
    file_type= models.CharField(max_length=5, null=False, blank=True)
    original_scan = models.CharField(max_length=5, null=False, blank=True)
    # whether it was orignal, scan or a copy 
    time_period = models.CharField(max_length=2, choices=TimePeriod.choices, default="JU")
    origin_date = models.DateField(auto_now_add=False, null=False, blank=False, default=date(1970, 1, 1))
    author = models.CharField(max_length=40)
    size = models.IntegerField(null=True, blank=True)
    # file size
    description = models.CharField(max_length=1500, null=True, blank=True)
    source = models.CharField(max_length=50,null=False,blank=False)
    signature = models.CharField(max_length=20, null=False, blank=False)
    copyright_status = models.CharField(max_length=10, null=False, blank=False)
    current_location = models.CharField(max_length=20, null=False, blank=True)
    found_by = models.CharField(max_length=30, null=False, blank=True)
    found_date = models.DateField(null=False, blank=False, default=date(1970, 1, 1))
    production_date = models.DateField(null=False, blank=False, default=date(1970, 1, 1))
    additional_info = models.CharField(max_length=500, null=True, blank=True)

class Videos(models.Model):

    def file_upload_location(self, filename):
        return f"{self.related_site.serial_number}/videos/{filename}"

    related_site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="videos")
    name = models.CharField(max_length=50, null=True)
    video = models.FileField(upload_to=file_upload_location)

class Photos(models.Model):

    def file_upload_location(self, filename):
        return f"{self.related_site.serial_number}/photos/{filename}"

    name = models.CharField(max_length=50, null=True)
    related_site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="photos")
    photo = models.FileField(upload_to=file_upload_location)

def photo_cleanup(sender, instance, **kwargs):
    file_location = instance.photo.name
    os.remove(os.path.join(settings.MEDIA_ROOT, file_location))

def video_cleanup(sender, instance, **kwargs):
    file_location = instance.video.name
    os.remove(os.path.join(settings.MEDIA_ROOT, file_location))

post_delete.connect(photo_cleanup, sender=Photos)
post_delete.connect(video_cleanup, sender=Videos)