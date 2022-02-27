from django.contrib import admin

# Register your models here.

from .models import Photo, Category, Location

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Location)
