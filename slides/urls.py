from django.conf.urls.defaults import *
from laika.slides.models import Slide

urlpatterns = patterns('',
	(r'^slide/(?P<slug>[-\w]+)', 'laika.slides.views.slide'),
	(r'^/*', 'laika.slides.views.index'),
)
