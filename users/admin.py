import os

# Register your models here
if os.getenv("LOCAL_DEVELOPMENT", None) is not None:
    from django.contrib import admin
    from .models import User
    admin.site.register(User)