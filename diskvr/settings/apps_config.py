# Application definitions


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor_uploader',
]

PACKAGE_APPS = [
    'django_extensions',
]

ADDITIONAL_APPS = [
    'core',
    'inventory',
]

INSTALLED_APPS = DJANGO_APPS + PACKAGE_APPS + ADDITIONAL_APPS