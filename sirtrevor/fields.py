import json
from django.db import models
from django.template.loader import render_to_string
from django.utils.six import with_metaclass
from django.utils.translation import ugettext_lazy as _
from .forms import SirTrevorFormField


class SirTrevorContent(str):
    @property
    def html(self):
        html = []
        content = json.loads(self)
        for block in content['data']:
            template_name = 'sirtrevor/blocks/%s.html' % block['type']
            html.append(render_to_string(template_name, block['data']))
        return ''.join(html)


class SirTrevorField(with_metaclass(models.SubfieldBase, models.Field)):
    description = _("TODO")

    def get_internal_type(self):
        return 'TextField'

    def formfield(self, **kwargs):
        defaults = {
            'form_class': SirTrevorFormField
        }
        defaults.update(kwargs)
        return super(SirTrevorField, self).formfield(**defaults)

    def to_python(self, value):
        return SirTrevorContent(value)
