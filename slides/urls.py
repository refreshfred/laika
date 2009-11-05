from django.conf.urls.defaults import *
from laika.slides.models import Slide

query_dict = {
	'queryset': Slide.objects.filter(status=1), # We only want to pull Slides that are "done", no drafts.
}

urlpatterns = patterns('',
	(r'^/*', 'laika.slides.views.index'),
)
