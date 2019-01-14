from django.contrib import admin

# Register your models here.
from .models import Blog, FM

admin.site.register(Blog)
admin.site.register(FM)
