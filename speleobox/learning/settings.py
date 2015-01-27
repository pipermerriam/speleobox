DEBUG = False

SECRET_KEY = 'not-a-real-secret-key'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'NAME': 'speleobox',
    },
}


INSTALLED_APPS = (
    'speleobox.learning',
)
