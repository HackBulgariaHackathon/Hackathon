from django.conf.urls import patterns, url
from django.conf import settings
from . import views

urlpatterns = patterns('wiki.views',
    url(r'^wiki/$', 'show_wiki', name='wiki'),
    url(r'text/(?P<wiki_id>[0-9]+)/$', 'show_text', name='text'),
)
