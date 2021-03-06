import os
import django_heroku
import dj_database_url
from dotenv import load_dotenv
from os.path import join, dirname


# if os.name == 'nt':
#     import platform
#     OSGEO4W = r"C:\\OSGeo4W"
#     if '64' in platform.architecture()[0]:
#         OSGEO4W += "64"
#     assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
#     os.environ['OSGEO4W_ROOT'] = OSGEO4W
#     os.environ['GDAL_DATA'] = OSGEO4W + r"\share\\gdal"
#     os.environ['PROJ_LIB'] = OSGEO4W + r"\share\\proj"
#     os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
#     GDAL_LIBRARY_PATH = 'C:\\OSGeo4W64\\bin\\gdal204.dll'

# GDAL_LIBRARY_PATH = 'C:\\OSGeo4W64\\bin\\gdal204.dll'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL="/media/"

# GEOS_LIBRARY_PATH = 'C:\\OSGeo4W64\\bin\\geos_c.dll'

SECRET_KEY = 'wu=6z7$7)=7d#1vprblo3sjrsrh*q7d_x22r41s2q&os+melq4'

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1','shopsnearyou.herokuapp.com']

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'djgeojson',
    'jsonfield',
    'shops',
    'crispy_forms',
    'whitenoise.runserver_nostatic',
    'django_postgres_extensions',
    'django.contrib.postgres',
    'rest_framework',
    'rest_framework.authtoken',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres1',
        'USER': 'postgres',
        'PASSWORD': 'hello@213',
        'HOST': 'localhost',
        'PORT': os.getenv('DB_PORT')
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
ENABLE_ARRAY_M2M = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [os.path.join(BASE_DIR,'shops/static')
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'




# Email config
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER='healthymeal2021@gmail.com'
EMAIL_HOST_PASSWORD='healthy@213'
EMAIL_USE_TLS=True





django_heroku.settings(locals())
