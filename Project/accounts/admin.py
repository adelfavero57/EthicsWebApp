from django.contrib import admin

# Register your models here.

from .models import NormalUser

admin.site.register(NormalUser)

