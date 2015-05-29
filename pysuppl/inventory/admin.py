from django.contrib import admin


from .models import Software,Computer, License, Vendor


class SoftwareAdmin(admin.ModelAdmin):
        pass

class VendorAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'phone')

class ComputerAdmin(admin.ModelAdmin):
        exclude = ('name',)

class LicenseAdmin(admin.ModelAdmin):
        list_display = ('number', 'name', 'expire')


admin.site.register(Software, SoftwareAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Computer, ComputerAdmin)
