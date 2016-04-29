from django.contrib.staticfiles.storage import ManifestFilesMixin
from pipeline.storage import PipelineMixin
from storages.backends.s3boto import S3BotoStorage
from os import getenv
import urllib
from django.utils.six.moves.urllib.parse import (
    quote, urldefrag, urlsplit, urlunsplit,
)

class ManifestFilesMixinUrlEncoded(ManifestFilesMixin):
	def url(self, name, force=False):

		final_url = super(ManifestFilesMixinUrlEncoded, self).url(name, force)

		urlparts = list(urlsplit(final_url))
		urlparts[1] = getenv('AWS_CLOUDFRONT_URL')
		url_queries = urlparts[3]
		query_pairs = url_queries.split('&')

		encoded_queries = []
		for query in query_pairs:
			key, val = query.split('=', 1)

			encoded_queries.append(
				key + '=' + quote(val)
			)
		urlparts[3] ='&'.join(encoded_queries)
		final_url = urlunsplit(urlparts)

		return final_url

class S3PipelineManifestStorage(PipelineMixin, ManifestFilesMixinUrlEncoded, S3BotoStorage):
    pass