from django import forms
from sirtrevor.widgets import SirTrevorWidget


class ContentForm(forms.Form):
    headline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=SirTrevorWidget(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=[(0, 'unpublished'),(1, 'public')], widget=forms.Select(attrs={'class': 'form-control'}))
