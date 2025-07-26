from .base import *
from dotenv import load_dotenv
from personal_site.settings import get_secret

load_dotenv(BASE_DIR / "steyaertsite" / "settings" / ".env")

DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = get_secret("SECRET_KEY", "")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static Files URL
STATIC_URL = "/static/"

# Media Files URL
MEDIA_URL = "/media/"

