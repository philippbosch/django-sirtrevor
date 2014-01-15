from django import forms
from .widgets import SirTrevorWidget


class SirTrevorFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        self.widget = SirTrevorWidget()
        super(SirTrevorFormField, self).__init__(*args, **kwargs)
