from inspect import signature
from django.db import models
from datetime import date

# Create your models here.

class Site(models.Model):
    time_period_choices = [
        ("FL" ,"Flakkaserne and before"),
        ("G1", "Grohn Barracks I"),
        ("DP",  "DP Camp Grohn"),
        ("G2", "Grohn Barracks II"),
        ("RK", "Roland-Kaserne"),
        ("JU", "IUB-JU")
    ]

    serial_number = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=50, null=False)
    file_name = models.CharField(max_length=50, null=True, blank=True)
    preview = models.FileField()
    # type: file, max-size: 20MB (excludign VR and AR)
    file_type= models.CharField(max_length=5, null=False, blank=True)
    original_scan = models.CharField(max_length=5, null=False, blank=True)
    # whether it was orignal, scan or a copy 
    time_period = models.CharField(max_length=2, choices=time_period_choices, default="JU")
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