from django.contrib import admin
from django.template.defaultfilters import slugify

from laika.slides.models import Slide

class SlideAdmin(admin.ModelAdmin):
	fields = ('title', 'body', 'status')
	
	def save_model(self, request, obj, form, change):
		obj.slug = slugify(obj.title)
		obj.save()

admin.site.register(Slide, SlideAdmin)
