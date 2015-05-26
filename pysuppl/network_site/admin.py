from django.contrib import admin
from .models import Network, Host


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('ipnet', 'is_root', 'desctiption')


class HostAdmin(admin.ModelAdmin):
    list_display = ('ip_addr', 'macaddr', 'ip_net')

admin.site.register(Network, NetworkAdmin)
admin.site.register(Host, HostAdmin)
