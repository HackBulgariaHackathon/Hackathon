from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', 'index'),
    url(r'^show_all/$', views.show_all),
    url(r'^show_paten_list/$', views.show_paten_list),
]
