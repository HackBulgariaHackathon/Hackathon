from django.conf.urls import url
from .views import upload, index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^index$', index),
    url(r'^upload$', upload),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
