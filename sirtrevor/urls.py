try:  # pre 1.6
    from django.conf.urls.defaults import url, patterns
except ImportError:
    from django.conf.urls import url, patterns


urlpatterns = patterns(
    '',
    url(
        '^attachments/',
        'sirtrevor.views.attachment',
        name='sirtrevor_attachments',
    ),
)
