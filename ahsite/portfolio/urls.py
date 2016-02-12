from django.conf.urls import patterns, url

from portfolio.views import IndexList, ProjectDetail, PageView, WorkProjectList, WritingProjectList, WhoPageView, WherePageView

urlpatterns = patterns('',
    url(r'^$', IndexList.as_view(), name='index'),
    url(r'^work/$', WorkProjectList.as_view(), name='work'),
    url(r'^writings/$', WritingProjectList.as_view(), name='writings'),
    url(r'^whereabouts/$', WherePageView.as_view(), name='whereabouts'),
    url(r'^who-is/$', WhoPageView.as_view(), name='who'),
    url(r'^case-study/(?P<slug>[a-z0-9-]+)/$', ProjectDetail.as_view(), name='case_study'),
    url(r'^writing/(?P<slug>[a-z0-9-]+)/$', ProjectDetail.as_view(), name='writing'),
    url(r'^(?P<slug>[a-z0-9-]+)/$', PageView.as_view(), name='page'),
)