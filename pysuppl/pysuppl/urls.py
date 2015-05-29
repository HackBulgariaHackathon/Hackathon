from django.conf.urls import include, url
from django.contrib import admin
from network_site import urls as network_urls
from vehicle import urls as vehicle_urls
from docs import urls as docs_urls
from wiki import urls as wiki_urls
# from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(network_urls, namespace="network")),
    url(r'^vehicle/', include(vehicle_urls)),
    url(r'^docs/', include(docs_urls)),
    url(r'^wiki/', include(wiki_urls)),
] + static("/static/", document_root="/home/rastamandito/Documents/Django_laptop/Hackathon/pysuppl/pysuppl/static/ ")
