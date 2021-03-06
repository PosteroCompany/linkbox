"""
WSGI config for linkbox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .settings import ENV

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "linkbox.settings")

application = get_wsgi_application()

if ENV == 'Production':
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)
