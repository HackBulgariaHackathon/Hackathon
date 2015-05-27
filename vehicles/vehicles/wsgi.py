"""
<<<<<<< HEAD
WSGI config for mysite project.
=======
WSGI config for vehicles project.
>>>>>>> 2116fc8bc9018ca3554971ee77b09499d2b29c82

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vehicles.settings")

application = get_wsgi_application()
