
from django.contrib import admin

# Register your models here.

from .models import Vehicle, Paten_list


class VehicleAdmin(admin.ModelAdmin):
    vehicle_display = ('status', 'reserved', 'returned')


class Paten_listAdmin(admin.ModelAdmin):
    list_display = ('user', )

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Paten_list, Paten_listAdmin)
