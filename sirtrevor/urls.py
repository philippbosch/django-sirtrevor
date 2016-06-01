from sirtrevor.views import attachment

try:  # pre 1.6
    from django.conf.urls.defaults import url, patterns
except ImportError:
    from django.conf.urls import url, patterns


urlpatterns = [
    url(
        r'^attachments/',
        attachment,
        name='sirtrevor_attachments',
    ),
]
