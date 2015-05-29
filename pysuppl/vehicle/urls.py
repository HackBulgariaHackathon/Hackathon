from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', 'index'),
    url(r'^show_all/$', views.show_all),

]
