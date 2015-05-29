
from django.contrib import admin

# Register your models here.

from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    vehicle_display = ('number', 'status', 'user_id')

admin.site.register(Vehicle, VehicleAdmin)
