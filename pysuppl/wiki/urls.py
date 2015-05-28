
from django.conf.urls import paterns, url
# from .views import get_computers
from . import views

urlpatterns = [
    url(r'^$', 'show_wiki', name='wiki'),
    url(r'^wiki/(?P<wiki_id>[0-9]+)/$', 'show_text', name='show_text'),

