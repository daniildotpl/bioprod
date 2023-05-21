import os

from distutils import util
from pathlib import Path
from telnetlib import AUTHENTICATION
from dotenv import load_dotenv

load_dotenv()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_site',
    'app_status',
    'app_rearward',

    # ckeditor:
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'crm.wsgi.application'


# --- Password validation
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


# --- Internationalization (customise)
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = False
USE_TZ = True


# --- Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# -------- custom format date --------------
DATE_INPUT_FORMATS = ['%d.%m.%Y']
DATE_FORMAT = ['%d.%m.%Y']


### --------------- for CKEDITOR ----------------
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = os.getenv('ckeditorbasepath')
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Format',
             '-', 'Maximize',
             '-', 'Table',
             '-', 'Image',
             '-', 'Source',
             '-', 'NumberedList', 'BulletedList'
            ],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
             '-', 'Font', 'FontSize', 'TextColor',
             '-', 'Outdent', 'Indent',
             '-', 'HorizontalRule',
             '-', 'Blockquote'
            ]
        ],
        'height': 250,
        'width': '100%',
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True
    }
}
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True




##### ------------ for SMTP --------------
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'bioarttech@yandex.ru'
EMAIL_HOST_PASSWORD = '214365dex'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER






#### ------------- for AUTHUNTICATION -------------
AUTH_USER_MODEL = 'app_site.User'



# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379











##### --------------------------------------
##### --------- this is in env -------------
##### --------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('crm_dbname'),
        'USER': os.getenv('crm_dbuser'),
        'PASSWORD': os.getenv('crm_dbpass'),
        'HOST': 'localhost'
    }
}

MEDIA_URL = os.getenv('crm_mediaurl')
MEDIA_ROOT = os.getenv('crm_mediaroot')

STATIC_URL = os.getenv('crm_staticurl')
STATIC_ROOT = os.getenv('crm_staticroot')

DEBUG = bool(util.strtobool(os.getenv('crm_debug')))

ALLOWED_HOSTS = [os.getenv('crm_allowedhosts')]

SECRET_KEY = os.getenv('crm_seckey')

