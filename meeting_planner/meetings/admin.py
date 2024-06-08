from django.contrib import admin
from .models import Meeting,Room

# Register your models here.

# Aşağıdaki registration vasıtasıyla Meeting ve Room varlıklarının CRUD operasyonları için tek satır kod yazmadan Admin Paneli vasıtasıyla gerçekleştireceiğiz.
admin.site.register(Meeting)
admin.site.register(Room)