from django import forms
from sirtrevor.widgets import SirTrevorWidget
from .models import Content


class ContentForm(forms.Form):
    content = forms.CharField(
        widget=SirTrevorWidget(attrs={'class': 'form-control'})
    )


class ContentModelForm(forms.ModelForm):
    class Meta:
        model = Content
