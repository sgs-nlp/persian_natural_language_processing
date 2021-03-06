"""
Create by 'nvd' on '2021 July 12' Date.
"""

from pathlib import Path
import os
import logging
from nvd.base_dict import BaseDict

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5qsb__8uja28=swxp6_5z%z)6y7(=9x*o2e%&wia^tib=zi5rk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'persian_news_classification.apps.PersianNewsClassificationConfig',
    'statistical_pnc.apps.StatisticalPncConfig',
    'extra_settings.apps.ExtraSettingsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'classification.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'classification.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#       'default': {
#           'ENGINE': 'django.db.backends.postgresql_psycopg2',
#           'NAME': 'classification',
#           'USER': 'nvd',
#           'PASSWORD': 'nvd',
#           'HOST': 'localhost',
#           'PORT': '',
#       }
#   }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='.log',
    filemode='w',
    format='%(levelname)s - %(asctime)s - module: %(module)s - message: \"%(message)s\"'
)

# chashing
CASH_DICTIONARY = {}
BASE_DICT = BaseDict()

# caches
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379

# hazm tagger

# TAGGER = POSTagger(model='/home/ya_hasan_mojtaba/my_projects/resources/hazm/resources-0.5/postagger.model')

NEWS_CLASSIFICATION_BY_GENSIM_FILE_ROOT = os.path.join(MEDIA_ROOT, 'news_calassification_by_gensim_file.pkl')
NEWS_CLASSIFICATION_BY_STATISTICAL_FILE_ROOT = os.path.join(MEDIA_ROOT, 'news_calassification_by_statistical_file.pkl')