from settings import *
# from dossier.db_settings import DATABASE as DOSSIER, DATABASE_ROUTERS, read_setting

# DATABASES['dossier'] = DOSSIER

LOGGING["loggers"].update({
    'etl': {
        'handlers': ['mail_admins', 'console', default_handler],
        'formatter': 'verbose',
        'level': 'INFO',
        'propagate': True
    }
})

INSTALLED_APPS += ('etl')
