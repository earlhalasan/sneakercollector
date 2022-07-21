from django.contrib import admin

# Register your models here.
from .models import Sneaker, Release

admin.site.register(Sneaker)
admin.site.register(Release)