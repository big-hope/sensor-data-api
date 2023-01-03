from django.contrib import admin
from core.models import Device, SensorData


admin.site.register(SensorData)
admin.site.register(Device)
