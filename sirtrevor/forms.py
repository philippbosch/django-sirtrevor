from django import forms
from .widgets import SirTrevorWidget
from django import forms


class SirTrevorFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        self.widget = SirTrevorWidget()
        super(SirTrevorFormField, self).__init__(*args, **kwargs)


class AttachmentForm(forms.Form):
    attachment = forms.FileField()
