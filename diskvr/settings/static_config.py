import os
from .base import BASE_DIR


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'