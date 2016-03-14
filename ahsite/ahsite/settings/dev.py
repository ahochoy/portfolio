from os.path import join, normpath, dirname
from os import getenv
from base_settings import *
from configobj import ConfigObj

########## DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
########## END ALLOWED HOST CONFIGURATION
