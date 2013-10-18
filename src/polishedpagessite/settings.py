""" Django settings for polishedpagessite project. """
import os
from django.core.exceptions import ImproperlyConfigured

# Try to import local settings.
try:
    from .local_settings import (DATABASES, LOGGING, DEBUG, TEMPLATE_DEBUG,
        ADMINS, MANAGERS, TIME_ZONE, LANGUAGE_CODE, SITE_ID,
        USE_I18N, USE_L10N, USE_TZ,
        MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATICFILES_DIRS)
except ImportError as ex:
    raise ImproperlyConfigured('Could not import local_settings. '
        'Make sure you have created a local_settings file. ({})'.format(ex))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y!(tbtiq&amp;i8rj2^$&amp;wc&amp;p@h)@awb=ysj-g3i^bjs@9q26q=nlq'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'polishedpagessite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'polishedpagessite.wsgi.application'

INSTALLED_APPS = (
    # django.contrib
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # external/3rd party
    'south',
    'rest_framework',

    # in-house
    'polishedpages',
)

_SITE_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

try:
    TEMPLATE_DIRS = TEMPLATE_DIRS + (_SITE_TEMPLATE_DIR,)
except NameError:
    TEMPLATE_DIRS = (_SITE_TEMPLATE_DIR,)

# Custom user model
AUTH_USER_MODEL = 'polishedpages.BasicUser'
