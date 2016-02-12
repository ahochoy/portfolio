from django.contrib import admin
from portfolio.models import Project, Company, Field, Page, ProjectImage, Award

class ProjectImageInline(admin.StackedInline):
	model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
		('Project Details', {'fields': ['type', 'title', 'subtitle', 'slug', 'publish_date', 'featured' ]}),
		('Content', {'fields': ['work_url', 'code_url', 'body', 'video']}),
		('Social Graph Attributes', {'fields': ['rundown', 'functions', 'stakeholders']}),
		('Awards', {'fields': ['awards']}),
		('Additional Details', {'fields': ['related_projects', 'hex_color']})
	]

	list_filter = ('type', 'publish_date')

	list_display = ['title', 'type', 'publish_date', 'featured']
	
	inlines = [ProjectImageInline]

admin.site.register(Page)
admin.site.register(Award)
admin.site.register(Field)
admin.site.register(Company)
admin.site.register(Project, ProjectAdmin)