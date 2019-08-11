"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from decouple import config
from environ import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = Path(__file__) - 3

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]


# Third Party apps

INSTALLED_APPS += [
    'rest_framework',
    'drf_yasg',
    'rest_auth',
    'corsheaders',
    'phonenumber_field',
]


# Project apps

INSTALLED_APPS += [
    'accounts.apps.AccountsConfig',
    'shared.apps.SharedConfig',
    'profiles.apps.ProfilesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# MYSQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
        'TEST': {
            'CHARSET': 'utf8mb4'
        }
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Addis_Ababa'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')


# Custom Auth User Model

AUTH_USER_MODEL = 'accounts.CustomUser'


# Authentications

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.PhoneNumberBackend'
]


# Cors Headers

CORS_ORIGIN_ALLOW_ALL = True

# Site ID

SITE_ID = 1


# DRF

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ]
}


# JWT

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'accounts.utilities.jwt_response_payload_handler',
}


# Django Phonenumber Field

PHONENUMBER_DEFAULT_REGION = 'ET'


# SMS

DEFAULT_SMS_PROVIDER = 'shared.sms.providers.AfricasTalking'

# Africastalking

AFRICASTALKING_API_USERNAME = config('AFRICASTALKING_API_USERNAME')
AFRICASTALKING_API_KEY = config('AFRICASTALKING_API_KEY')
AFRICASTALKING_SHORT_CODE = config('AFRICASTALKING_SHORT_CODE')
