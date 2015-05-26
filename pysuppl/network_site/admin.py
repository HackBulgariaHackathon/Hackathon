from django.contrib import admin
from .models import Network, Host, NetworkDevice, NetworkEquipment, NetworkProt, Vlan


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('ipnet', 'is_root', 'desctiption')


class HostAdmin(admin.ModelAdmin):
    list_display = ('ip_addr', 'macaddr', 'ip_net', 'device', 'host_name')


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_type', )


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_type', 'number_of_ports', 'desctiption')


class VlanAdmin(admin.ModelAdmin):
    list_display = ('vlan_id', 'name')


class NetworkProtAdmin(admin.ModelAdmin):
    list_display = ('port_name', 'device', 'get_vlans', 'port_status')


admin.site.register(Network, NetworkAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(NetworkDevice, DeviceAdmin)
admin.site.register(NetworkEquipment, EquipmentAdmin)
admin.site.register(NetworkProt, NetworkProtAdmin)
admin.site.register(Vlan, VlanAdmin)
