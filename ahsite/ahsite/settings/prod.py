from os.path import join, normpath, dirname
from base_settings import *
from os import getenv
from S3 import CallingFormat

########## MAINTENANCE MODE CONFIGURATION
MAINTENANCE_MODE = False
########## END MAINTENANCE MODE CONFIGURATION

########## STATIC/MEDIA FILES CONFIGURATION
AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
AWS_HEADERS = {
	'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
	'Cache-Control': 'max-age=94608000',
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'ahsite.settings.pipeline_storage.S3PipelineManifestStorage'
########## END STATIC/MEDIA FILES CONFIGURATION

########## DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
ALLOWED_HOSTS = ['.andrewhochoy.com']
########## END ALLOWED HOST CONFIGURATION
