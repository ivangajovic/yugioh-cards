import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yugiohcards',
        'USER': 'ivan',
        'PASSWORD': 'ivan',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True
