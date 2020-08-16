
import dj_database_url

from .base                              import *


DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['www.heroku.com', 'btkweathers.herokuapp.com']

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header fro request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_XFORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
BASE_PATH = os.path.join(BASE_DIR)
APP_STATIC = 'weather/static/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_PATH, APP_STATIC)
#
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_PATH, f'{APP_STATIC}/media')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
