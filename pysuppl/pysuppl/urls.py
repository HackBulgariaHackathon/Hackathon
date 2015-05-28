from django.conf.urls import include, url
from django.contrib import admin
from network_site import urls as network_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(network_urls, namespace="network")),
]
