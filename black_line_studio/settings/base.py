import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# Application definition

ADMINS = (
            ('Sergey Funin', 'sfunin@gmail.com')
)

SITE_ID = 1

# INSTALLED_APPS = [
#     'home',
#     'search',
#     'django.contrib.sites',
#     'django_comments',
#     'django_comments_xtd',
#     'wagtail_react_streamfield',
#     'wagtail.contrib.forms',
#     'wagtail.contrib.redirects',
#     'wagtail.contrib.modeladmin',
#     'wagtailmenus',
#     'wagtail.embeds',
#     'wagtail.sites',
#     'wagtail.users',
#     'wagtail.snippets',
#     'wagtail.documents',
#     'wagtail.images',
#     'wagtail.search',
#     'wagtail.admin',
#     'wagtail',
#
#     'modelcluster',
#     'taggit',
#     'snowpenguin.django.recaptcha2',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'wagtailmetadata',
#     'wagtailtinymce',
#     'shops',
#     'blog',
#     'contact',
#     'django.contrib.sitemaps'
# ]

INSTALLED_APPS = [
    'snowpenguin.django.recaptcha2',
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.api.v2",
    "wagtail.locales",
    "wagtail.contrib.table_block",
    "wagtail.contrib.typed_table_block",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.simple_translation",
    "wagtail.contrib.styleguide",
    "wagtail",
    "rest_framework",
    "modelcluster",
    "taggit",
    "wagtailfontawesomesvg",
    "debug_toolbar",
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    'home',
    'shops',
    'blog',
    'contact',
    'search',
    'wagtailmenus'
]

RECAPTCHA_PRIVATE_KEY = '6LfAXvMbAAAAABVj0px-p_NPKl_7zcwIGdmT_G0i'
RECAPTCHA_PUBLIC_KEY = '6LfAXvMbAAAAAGhF3vCzWbDud1hOSGvZ8tkD5jJm'

# RECAPTCHA_PRIVATE_KEY = '6LchmigaAAAAANZI0_ysu8cyH_64npMCTuMGa1bQ'
# RECAPTCHA_PUBLIC_KEY = '6LchmigaAAAAAO2bZQIuiHA8aQOvYrpJz2AMafpU'
# RECAPTCHA_DEFAULT_ACTION = 'generic'
# RECAPTCHA_SCORE_THRESHOLD = 0.5


MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    'contact.middleware.contact_form_middleware',
]

ROOT_URLCONF = 'black_line_studio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
                'wagtailmenus.context_processors.wagtailmenus',
                'shops.context_processors.footer_shops',
                'home.context_processors.site_elements',
            ],
        },
    },
]

WSGI_APPLICATION = 'black_line_studio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'black_line_studio',
#         'USER': 'black_line_studio',
#         'HOST': '10.11.29.106',
#         'PASSWORD': '124AhCOtQrTp'
#     }
# }



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/#manifeststaticfilesstorage

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
    },
    'tinymce': {
        'WIDGET': 'wagtailtinymce.rich_text.TinyMCERichTextArea',
    }
}


# Wagtail settings

WAGTAIL_SITE_NAME = "Black Line Studios"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
# WAGTAILADMIN_BASE_URL = 'https://blacklinestudios.ca'
WAGTAILADMIN_BASE_URL = 'http://localhost:8002'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtpcorp.com'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'blacklinestudios'
EMAIL_HOST_PASSWORD = 'dG9qZXdiYmE4bDAw'


WAGTAILMENUS_ACTIVE_ANCESTOR_CLASS = 'active'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
