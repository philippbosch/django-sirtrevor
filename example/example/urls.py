from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'content.views.form_view'),
    url(r'^admin/', include(admin.site.urls)),
)
