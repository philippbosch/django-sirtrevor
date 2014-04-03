from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from content.views import PlainFormView, ModelFormView, ModelDisplayView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^form/$', PlainFormView.as_view(), name='form_view'),
    url(r'^model-form/$', ModelFormView.as_view(), name='model_form_view'),
    url(r'^model-form/(?P<pk>\d+)/$', ModelDisplayView.as_view(), name='model_display_view'),
    url(r'^sirtrevor/', include('sirtrevor.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
