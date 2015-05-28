from django.conf.urls import url
# from .views import get_computers
from . import views

urlpatterns = [
    # url(r'^$', 'index'),
    url(r'^computers$', views.get_computers),
    url(r'^show_computer/$', views.get_computer_info),
    url(r'^new_computer/$', views.new_computer),
    url(r'^add_computer/$', views.add_computer),
    # url(r'^show_computer/$', views.delete_computer),
    url(r'^(?P<computer_id>[0-9]+)/delete/$',
        views.delete_computer, name='delete_computer'),
    url(r'^(?P<computer_id>[0-9]+)/edit/$',
        views.edit_computer, name='edit_computer'),
    # url(r'^/edit/$',
    #     views.edit_computer, name='edit_computer'),
]
