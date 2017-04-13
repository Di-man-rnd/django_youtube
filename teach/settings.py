"""
Django using Django 1.9.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '_dlbu82kz90g=il(w@zenmqumj*w=)icmtng*302=x%enz@=i!'

DEBUG = True
TEMPLATE_DEBUG = False
SITE_ID = 1
# отправлять емэил на почту при ошибках
# ADMINS = (
#     ('name', 'E-mail'),
#     ('name', 'E-mail'),
# )
# EMAIL_HOST =



# Настройка оповещения о «битых» ссылках
# SEND_BROKEN_LINK_EMAILS = True

MANAGERS = (
    ('name', 'E-mail'),
    ('name', 'E-mail'),
)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'books',
    'youtube',
    'blog',

    'django.contrib.flatpages',
    'django.contrib.sites',
    'tinymce',
    'ckeditor',
    'ckeditor_uploader',
    # 'gunicorn',
]


CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'height': 391,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'div', 'autolink', 'autoembed', 'embedsemantic', 'autogrow', 'devtools',
            'widget', 'lineutils', 'clipboard', 'dialog', 'dialogui', 'elementspath',
            'a11yhelp',  'adobeair', 'ajax', 'autoembed', 'autogrow', 'autolink',
            'clipboard', 'codesnippet','codesnippetgeshi', 'colordialog', 'devtools',
            'dialog', 'div', 'divarea', 'docprops', 'embed', 'embedbase','embedsemantic',
            'filetools', 'find', 'flash', 'forms', 'iframe', 'iframedialog', 'image',
            'image2', 'language','lineutils', 'link', 'liststyle', 'magicline', 'mathjax',
            'menubutton', 'notification', 'notificationaggregator','pagebreak', 'pastefromword',
            'placeholder', 'preview', 'scayt', 'sharedspace', 'showblocks', 'smiley','specialchar',
            'stylesheetparser', 'table', 'tableresize', 'tabletools', 'templates', 'uicolor',
            'uploadwidget', 'widget', 'wsc', 'xml']
        ),
    }
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.gzip.GZipMiddleware', # сжимает ответы для экономии пропускной способности
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'teach.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],     ###:  os.path.join(BASE_DIR, 'templates')
        'APP_DIRS': True,   # смотреть в приложении потом в проекте
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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/home/Bondarenko/PycharmProjects/learn/test/teach/cache',
        # 'TIMEOUT': 300, None в timeout можно закэшировать данные навсегда,  0 значение никогда не будет кэшироваться
    }
}


WSGI_APPLICATION = 'teach.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'ru-RU'  ###: 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/files/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')

TEMPLATE_DIRS = [BASE_DIR + '/templates']
LOG_PATH = BASE_DIR + '/log.txt'




# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = BASE_DIR
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'





# INSTALLED_APPS += ("djcelery", )
# адрес redis сервера
BROKER_URL = 'amqp://admin:admin@127.0.0.1:5672/'
# храним результаты выполнения задач так же в redis
CELERY_RESULT_BACKEND = 'amqp://admin:admin@127.0.0.1:5672/'
# в течение какого срока храним результаты, после чего они удаляются
CELERY_TASK_RESULT_EXPIRES = 7*86400  # 7 days
# это нужно для мониторинга наших воркеров
CELERY_SEND_EVENTS = True
# место хранения периодических задач (данные для планировщика)
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
# в конец settings.py добавляем строчки
import djcelery
djcelery.setup_loader()