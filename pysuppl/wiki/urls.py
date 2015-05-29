from django.conf.urls import patterns, url
from django.conf import settings
from . import views

# urlpatterns = patterns('wiki.views',
#     url(r'^wiki/$', 'show_wiki', name='wiki'),
#     url(r'text/(?P<wiki_id>[0-9]+)/$', 'show_text', name='text'),
# )


urlpatterns = [
    url(r'^show_wiki/$', views.show_wiki),
    url(r'text/(?P<wiki_id>[0-9]+)/$', views.show_text)
]

