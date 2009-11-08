import settings, os.path
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

	# The following line isn't best practice, I'm just lazy - you should try not to catch all for one specific app.
    (r'^laika/', include('laika.slides.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('django.views.static',
		(r'^static_media/(?P<path>.*)$', 'serve', {'document_root': os.path.join(os.path.dirname(__file__), 'static/'), 'show_indexes': True }),
	)
