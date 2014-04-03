import json
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import force_text


class SirTrevorWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        if 'attrs' not in kwargs:
            kwargs['attrs'] = {}
        class_list = kwargs['attrs'].get('class', '').split()
        class_list.append('js-st-instance')
        kwargs['attrs']['class'] = ' '.join(class_list)

        sirtrevor_conf = {
            'blockTypes': kwargs.pop('st_block_types', settings.SIRTREVOR_BLOCK_TYPES),
            'defaultType': kwargs.pop('st_default_type', settings.SIRTREVOR_DEFAULT_TYPE),
            'blockLimit': kwargs.pop('st_block_limit', settings.SIRTREVOR_BLOCK_LIMIT),
            'blockTypeLimits': kwargs.pop('st_block_type_limits', settings.SIRTREVOR_BLOCK_TYPE_LIMITS),
            'required': kwargs.pop('st_required', settings.SIRTREVOR_REQUIRED),
        }
        kwargs['attrs']['data-sirtrevor-conf'] = json.dumps(sirtrevor_conf)

        super(SirTrevorWidget, self).__init__(*args, **kwargs)

    def build_attrs(self, extra_attrs=None, **kwargs):
        attrs = super(SirTrevorWidget, self).build_attrs(extra_attrs, **kwargs)

        sirtrevor_defaults = {
            'uploadUrl': kwargs.pop('st_upload_url', force_text(settings.SIRTREVOR_UPLOAD_URL)),
        }
        attrs['data-sirtrevor-defaults'] = json.dumps(sirtrevor_defaults)

        return attrs

    class Media:
        js = [
            'sirtrevor/components/jquery/jquery.min.js',
            'sirtrevor/components/underscore/underscore-min.js',
            'sirtrevor/components/Eventable/eventable.js',
            'sirtrevor/components/sir-trevor-js/sir-trevor.js',
            'sirtrevor/init.js',
        ]
        css = {
            'all': [
                'sirtrevor/components/sir-trevor-js/sir-trevor.css',
                'sirtrevor/components/sir-trevor-js/sir-trevor-icons.css',
            ]
        }
