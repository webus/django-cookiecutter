from dynaconf import settings as dyn_settings

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': dyn_settings.get('POSTGRES_DB'),
        'USER': dyn_settings.get('POSTGRES_USER'),
        'PASSWORD': dyn_settings.get('POSTGRES_PASSWORD'),
        'HOST': dyn_settings.get('DJANGO_DATABASE_HOST'),
        'PORT': dyn_settings.get('DJANGO_DATABASE_PORT', 5432),
        'CONN_MAX_AGE': dyn_settings.get('CONN_MAX_AGE', 60),
        'OPTIONS': {
            'connect_timeout': 10
        }
    }
}
