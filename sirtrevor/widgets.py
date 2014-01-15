import json
from django import forms
from .conf import settings


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
        kwargs['attrs']['data-sirtrevor'] = json.dumps(sirtrevor_conf)

        super(SirTrevorWidget, self).__init__(*args, **kwargs)

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
