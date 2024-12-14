import logging, sys, datetime
from logging import config
from django.conf import settings

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': 'AppSeed: %(levelname)s %(message)s'
            },
        },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
            },
        },
    'loggers': {
        'my-logger': {
            'handlers': ['stdout'],
            'level': logging.DEBUG,
            'propagate': True,
            },
        }
    }

config.dictConfig(LOGGING) 

def logger(aText, aLevel=logging.DEBUG):

    if logging.DEBUG == aLevel:
        print( f'{datetime.datetime.now()} - AppSeed-{settings.VERSION}, DEBUG {aText}'    )
    elif logging.WARN == aLevel:    
        print( f'{datetime.datetime.now()} - AppSeed-{settings.VERSION}, WARN {aText}'     )
    elif logging.ERROR == aLevel:    
        print( f'{datetime.datetime.now()} - AppSeed-{settings.VERSION}, ERROR {aText}'    )
    elif logging.CRITICAL == aLevel:    
        print( f'{datetime.datetime.now()} - AppSeed-{settings.VERSION}, CRITICAL {aText}' )
    else: 
        print( f'{datetime.datetime.now()} - AppSeed-{settings.VERSION}, INFO {aText}'     )

def logger_info(aText):
    logger(aText, aLevel=logging.INFO)

def logger_warn(aText):
    logger(aText, aLevel=logging.WARN)

def logger_err(aText):
    logger(aText, aLevel=logging.ERROR)

def logger_error(aText):
    logger(aText, aLevel=logging.ERROR)

def logger_critical(aText):
    logger(aText, aLevel=logging.CRITICAL)
