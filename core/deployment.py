from .settings import *
import os

SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = 'static'

STATIC_URL = 'static' # look for static inside APPS folder

STATICFILES_DIRS = [
   'challenges/static', # look outside APPs folder
   'static'
]

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
params = { code.split('='):code.split('=')[1] for code in connection_string}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': params['dbname'],
        'HOST': params['host'],
        'USER': params['user'],
        'PASSWORD': params['password'],
    }
}