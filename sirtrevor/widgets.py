from django import forms


class SirTrevorWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        if 'attrs' not in kwargs:
            kwargs['attrs'] = {}
        class_list = kwargs['attrs'].get('class', '').split()
        class_list.append('js-st-instance')
        kwargs['attrs']['class'] = ' '.join(class_list)
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
