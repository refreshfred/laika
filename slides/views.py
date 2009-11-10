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
	next_slide = {}
	previous_slide = {}
	
	# It's 5AM, the following two lines of code are a bad hack. Don't use them. ^_^ -- Ryan
	# In an ideal world, I'd set the model to have something to organize and reference by - an exercise for the reader, perhaps? ;)
	# If you make a solution, feel free to commit it back. :D
	try:
		next_slide = Slide.objects.get(id = (slide.id + 1))
	except:
		pass
	
	try:
		previous_slide = Slide.objects.get(id = (slide.id - 1))
	except:
		pass
	
	return render_to_response('laika/slide.html', {'slide': slide, 'next_slide': next_slide, 'previous_slide': previous_slide})
