from os.path import join, normpath, dirname
from os import getenv
from base_settings import *
from configobj import ConfigObj
from S3 import CallingFormat

########## MAINTENANCE MODE CONFIGURATION
MAINTENANCE_MODE = False
########## END MAINTENANCE MODE CONFIGURATION

########## DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## ASSET CONFIGURATION
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = getenv('S3_ACCESS_ID')
AWS_SECRET_ACCESS_KEY = getenv('S3_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = getenv('S3_BUCKET_NAME')
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}
########## END ASSET CONFIGURATION

########## STATIC FILE CONFIGURATION
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
########## END STATIC FILE CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
ALLOWED_HOSTS = ['.andrewhochoy.com']
########## END ALLOWED HOST CONFIGURATION
