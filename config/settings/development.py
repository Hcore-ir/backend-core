import os

# import local Modules
from .core import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-6s(k#g7gq6i^=n8r#61d!@^!uhaa_w1at5lpa(e1mc##yqrp73"
)
DEBUG = os.getenv("DEBUG", "True")

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Config the CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:*",
    "http://127.0.0.1:*",
]

# DRF Production Config
if DEBUG == True:
    REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = [
        "rest_framework.permissions.AllowAny",
    ]
