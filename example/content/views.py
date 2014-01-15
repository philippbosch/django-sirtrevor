import json
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import FormView, CreateView, DetailView
from sirtrevor import SirTrevorContent
from .forms import ContentForm, ContentModelForm
from .models import Content


TEST_CONTENT = {
    "data": [
        {
            "type": "heading",
            "data":{
                "text": "This is a headline"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut in geometria, prima si dederis, danda sunt omnia. Duo Reges: constructio interrete. Sin aliud quid voles, postea. Et harum quidem rerum facilis est et expedita distinctio.\n\nApud imperitos tum illa dicta sunt, aliquid etiam coronae datum; Itaque his sapiens semper vacabit."
            }
        },
        {
            "type": "quote",
            "data": {
                "cite": "Bill Gates",
                "text": "> 640k should be enough for everyone."
            }
        },
        {
            "type": "video",
            "data": {
                "source": "vimeo",
                "remote_id": "83511061"
            }
        },
        {
            "type": "list",
            "data": {
                "text": " - John Lennon\n - Paul McCartney\n - Ringo Starr\n - George Harrison\n"
            }
        }
    ]
}


class PlainFormView(FormView):
    form_class = ContentForm
    template_name = 'content/form.html'

    def form_valid(self, form):
        obj = {
            'content': SirTrevorContent(form.cleaned_data['content'])
        }
        return render(self.request, 'content/output.html', dict(object=obj))


class ModelFormView(CreateView):
    model = Content
    form_class = ContentModelForm
    template_name = 'content/form.html'

    def get_initial(self):
        return {'content': json.dumps(TEST_CONTENT)}

    def get_success_url(self):
        return reverse('model_display_view', args=[self.object.id])


class ModelDisplayView(DetailView):
    model = Content
    template_name = 'content/output.html'
