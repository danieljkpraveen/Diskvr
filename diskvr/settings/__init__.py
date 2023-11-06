import environ


env = environ.Env()
environ.Env.read_env()


SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ROOT_URLCONF = 'diskvr.urls'

WSGI_APPLICATION = 'diskvr.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from .apps_config import *
from .base import *
from .database_config import *
from .email_config import *
from .logger_config import *
from .login_urls_config import *
from .media_config import *
from .middleware_config import *
from .password_auth import *
from .static_config import *
from .templates_config import *