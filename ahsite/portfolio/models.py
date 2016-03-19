from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse 
from tinymce.models import HTMLField

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=50)
	url = models.URLField(blank=True)
	twitter_handle = models.CharField(max_length=25, blank=True)
	slug = models.SlugField(max_length=50)

	def twitter_url(self):
		twitter_base = "http://twitter.com/"
		if (re.search("^@", twitter_handle)):
			return twitter_base + twitter_handle[1:]
		else:
			return twitter_base + twitter_handle

	class Meta:
		verbose_name_plural = "companies"

	def __unicode__(self):
		return self.name

class Field(models.Model):
	name = models.CharField(max_length=25)
	slug = models.SlugField(max_length=50)

	def __unicode__(self):
		return self.name

class Award(models.Model):
	name = models.CharField(max_length=50)
	awarder = models.CharField(max_length=100)
	url = models.URLField(max_length=100, blank=True)
	date = models.DateField()

	def __unicode__(self):
		return self.name

class Project(models.Model):
	CASE = 'Case Study'
	ESSAY = 'Essay'
	WORK = 'Work'
	PROJECT_TYPE_CHOICES = (
		(CASE, 'Case Study'),
		(ESSAY, 'Essay'),
		(WORK, 'Work'),
	)
	stakeholders = models.ManyToManyField(Company, blank=True, null=True)
	body = HTMLField()
	type = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=20, default=ESSAY)
	rundown = models.TextField()
	related_projects = models.ManyToManyField('self', blank=True, null=True)
	video = models.TextField(blank=True, null=True)
	awards = models.ManyToManyField(Award, blank=True, null=True)
	publish_date = models.DateField()
	functions = models.ManyToManyField(Field)
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=100)
	slug = models.SlugField(max_length=50)
	work_url = models.URLField(max_length=100, blank=True)
	code_url = models.URLField(max_length=100, blank=True)
	hex_color = models.CharField(max_length=6, default='000000', blank=True)
	featured = models.BooleanField(default=None)

	def featured_images(self):
		return self.images.filter(featured=True)

	def non_featured_images(self):
		return self.images.filter(featured=False)

	def get_absolute_url(self):
		path_prefix = u'/writing' if self.type == 'Essay' else u'/case-study'
		return path_prefix + u'/' + self.slug

	def __unicode__(self):
		return self.title
	
class ProjectImage(models.Model):
	project = models.ForeignKey('Project', related_name='images')
	image = models.ImageField(upload_to='portfolio/%Y/%m')
	title = models.CharField(max_length=100)
	caption = models.CharField(max_length=200, blank=True)	
	featured = models.BooleanField(default=None)

	def __unicode__(self):
		return self.image.name

class Page(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=50)
	content = HTMLField()	
	background_color = models.CharField(max_length=6, blank=True)
	visible = models.BooleanField(default=None)
	show_breadcrumb = models.BooleanField(default=True)
	custom_css = models.TextField(blank=True)

	def __unicode__(self):
		return self.title