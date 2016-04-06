from os.path import join, normpath, dirname
from os import getenv
from base_settings import *
from configobj import ConfigObj

########## STATIC/MEDIA FILES CONFIGURATION
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
########## END STATIC/MEDIA FILES CONFIGURATION

########## DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
ALLOWED_HOSTS = ['*']
########## END ALLOWED HOST CONFIGURATION
