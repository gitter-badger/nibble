import dj_database_url

from .base import *

DEBUG = False

DATABASES['default'] = dj_database_url.config()

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
