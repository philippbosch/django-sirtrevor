from django import forms
from django.db import models
from sirtrevor.widgets import SirTrevorWidget
from .models import Content


class ContentForm(forms.Form):
    headline = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        widget=SirTrevorWidget(attrs={'class': 'form-control'})
    )


class ContentModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContentModelForm, self).__init__(*args, **kwargs)
        self.fields['headline'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Content
