from django.shortcuts import render
from .forms import ContentForm


def form_view(request):
    if request.method == 'POST':
        return render(request, 'content/output.html', dict(data=request.POST))
    else:
        return render(request, 'content/form.html', dict(form=ContentForm()))
