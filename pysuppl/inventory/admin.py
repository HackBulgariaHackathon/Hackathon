#! -*- coding: utf-8 -*-

from django.contrib import admin


# Register your models here.
from .models import Software, Computer, License, Vendor


class SoftwareAdmin(admin.ModelAdmin):

    list_display = ('name', )


class VendorAdmin(admin.ModelAdmin):

    ''' DOC STRING HERE '''

    list_display = ('name', 'email', 'phone', )


class ComputerAdmin(admin.ModelAdmin):

    ''' DOC STRING HERE '''

    exclude = ('name', )


class LicenseAdmin(admin.ModelAdmin):

    ''' DOC STRING HERE '''

    list_display = ('number', 'name', 'expire', )


admin.site.register(Software, SoftwareAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Computer, ComputerAdmin)
