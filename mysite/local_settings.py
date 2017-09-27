import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ygocard',
        'USER': 'ivan',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True
