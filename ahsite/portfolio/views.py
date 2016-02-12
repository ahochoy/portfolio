import datetime
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from portfolio.models import Project, Page, Company, Field

class IndexList(ListView):
	model = Project
	template_name = 'portfolio/index.html'

	def get(self, request, *args, **kwargs):
		self.featured_items = Project.objects.all().filter(featured=True).exclude(type='Work').exclude(publish_date__gt=datetime.date.today()).order_by('-publish_date')[:5]
		return super(IndexList, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(IndexList, self).get_context_data(**kwargs)
		context['featured_items'] = self.featured_items
		return context

class WorkProjectList(ListView):
	queryset = Project.objects.filter(type='Work').exclude(publish_date__gt=datetime.date.today()).select_related().order_by('-publish_date')[:5]
	context_object_name = 'projects'
	template_name = 'portfolio/list.html'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(WorkProjectList, self).get_context_data(**kwargs)
		context['title'] = u'Work'
		context['quip'] = u'The things people do for money.'
		return context

class WritingProjectList(ListView):
	queryset = Project.objects.filter(type='Essay').select_related()
	context_object_name = 'projects'
	template_name = 'portfolio/list.html'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(WritingProjectList, self).get_context_data(**kwargs)
		context['title'] = u'Writings'
		context['quip'] = u'"The first draft of anything is shit." -Ernest'
		return context

class ProjectDetail(DetailView):
	model = Project
	context_object_name = 'project'
	template_name = 'portfolio/detail.html'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(ProjectDetail, self).get_context_data(**kwargs)
		context['related_projects'] = Project.objects.exclude(slug=self.object.slug).exclude(type='Work').order_by('?')[:1]
		return context

class PageView(DetailView):
	model = Page
	context_object_name = 'page'
	template_name = 'portfolio/page.html'

class WhoPageView(TemplateView):
	model = Page
	template_name = 'portfolio/who.html'

class WherePageView(TemplateView):
	model = Page
	template_name = 'portfolio/whereabouts.html'
