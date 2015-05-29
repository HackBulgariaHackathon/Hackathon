"""pysuppl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import include, url
#from django.conf import settings
#from django.contrib import admin
#from django.conf.urls.static import static
#
#import inventory.urls as inventory_urls
#import docs.urls as docs_urls
#
#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^inventory/', include(inventory_urls)),
#    url(r'^docs/', include(docs_urls))
#]
#
#
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import include, url
from django.contrib import admin
from network_site import urls as network_urls
from vehicle import urls as vehicle_urls
from docs import urls as docs_urls
from wiki import urls as wiki_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(network_urls, namespace="network")),
    url(r'^vehicle/', include(vehicle_urls)),
    url(r'^docs/', include(docs_urls)),
    url(r'^wiki/', include(wiki_urls)),
] + static("/static/", document_root="/home/rastamandito/Documents/Django_laptop/Hackathon/pysuppl/pysuppl/static/ ")

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
