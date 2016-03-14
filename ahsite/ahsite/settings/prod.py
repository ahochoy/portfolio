from os.path import join, normpath, dirname
from os import getenv
from base_settings import *
from configobj import ConfigObj

########## MAINTENANCE MODE CONFIGURATION
MAINTENANCE_MODE = False
########## END MAINTENANCE MODE CONFIGURATION

########## DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
ALLOWED_HOSTS = ['.andrewhochoy.com']
########## END ALLOWED HOST CONFIGURATION
