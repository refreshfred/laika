from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail

from laika.slides.models import Slide

def index(request):
	queryset = Slide.objects.filter(status = 1) # We only wanna pull "published" slides, no drafts.
	return object_list(request, queryset, template_name='laika/index.html')

def slide(request, slug):
	slide = Slide.objects.get(slug = slug)
	return render_to_response('laika/slide.html', {'slide': slide})
