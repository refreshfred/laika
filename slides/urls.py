from django.conf.urls.defaults import *
from laika.slides.models import Slide

urlpatterns = patterns('django.views.generic.simple',
	(r'^/*', 'direct_to_template', {'template': 'laika/index.html'}),
)
