from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sites.models import Site
from django.contrib.sitemaps import Sitemap

from portfolio.views import IndexList, PageView, ProjectDetail, WorkProjectList, WritingProjectList
from portfolio.models import Project

import portfolio.urls

# Sitemap Setup
class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return obj.get_absolute_url

sitemaps = {
    'projects': ProjectSitemap,
}

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include(portfolio.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)