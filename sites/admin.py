import os

# Register your models here
if os.getenv("LOCAL_DEVELOPMENT", None) is not None:
    from django.contrib import admin
    from .models import Site, Photos, Videos
    admin.site.register(Site)
    admin.site.register(Photos)
    admin.site.register(Videos)
