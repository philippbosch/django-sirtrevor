from django.conf import settings
from appconf import AppConf


class SirTrevorConf(AppConf):
    BLOCK_TYPES = ['Text', 'List', 'Quote', 'Image', 'Video', 'Tweet', 'Heading']
    DEFAULT_TYPE = None
    BLOCK_LIMIT = 0
    BLOCK_TYPE_LIMITS = {}
    REQUIRED = []
