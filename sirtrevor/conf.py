from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from appconf import AppConf


class SirTrevorConf(AppConf):
    BLOCK_TYPES = ['Text', 'List', 'Quote', 'Image', 'Video', 'Tweet', 'Heading']
    DEFAULT_TYPE = None
    BLOCK_LIMIT = 0
    BLOCK_TYPE_LIMITS = {}
    REQUIRED = []
    UPLOAD_URL = None
    UPLOAD_PATH = 'attachments'
    ATTACHMENT_PROCESSOR = None
    MARKDOWN_EXTENSIONS = []

    def configure_upload_url(self, value):
        if value is not None:
            return value
        return reverse_lazy('sirtrevor_attachments')
