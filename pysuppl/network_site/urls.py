from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import index, site_logout, site_login

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^logout/$", site_logout, name="logout"),
    url(r"^login/$", site_login, name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
