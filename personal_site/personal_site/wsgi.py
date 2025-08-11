from os import environ

from django.core.wsgi import get_wsgi_application
from django.core.handlers.wsgi import WSGIHandler

environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_site.settings")

application: WSGIHandler = get_wsgi_application()
