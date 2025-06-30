import os

# import local Modules
from .core import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False")

# For production: specify your domain(s) for security
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(" ")

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

if os.getenv("DB_ENGINE_NAME", False):
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DB_ENGINE_NAME", "django.db.backends.postgresql"),
            "NAME": os.environ.get("DB_NAME", "h-core-api"),
            "USER": os.environ.get("DB_USER", "h-core-api"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "h-core-api"),
            "HOST": os.environ.get("DB_HOST", "127.0.0.1"),
            "PORT": os.environ.get("DB_PORT", "5432"),
            "TEST": {
                "NAME": "ewallet_test",
                "MIGRATE": False,
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Config the CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://admin.laiteclab.ir",
]

# DRF Production Config
core.REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = [
    "rest_framework.permissions.IsAuthenticatedOrReadOnly",
]
