from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^laika/', include('laika.slides.urls')),
    (r'^admin/', include(admin.site.urls)),
)
