import json
from django.template.loader import render_to_string

__version__ = (0, 1, 2)

class SirTrevorContent(str):
    @property
    def html(self):
        html = []
        content = json.loads(self)
        for block in content['data']:
            template_name = 'sirtrevor/blocks/%s.html' % block['type']
            html.append(render_to_string(template_name, block['data']))
        return ''.join(html)


