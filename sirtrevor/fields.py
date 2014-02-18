import json
from django.db import models
from django.conf import settings
from django.utils.six import with_metaclass
from django.utils.translation import ugettext_lazy as _
from . import SirTrevorContent
from .forms import SirTrevorFormField


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


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^sirtrevor\.fields\.SirTrevorField"])
