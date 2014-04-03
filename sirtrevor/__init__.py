import json
from django.template.loader import render_to_string
import six


class SirTrevorContent(six.text_type):
    @property
    def html(self):
        html = []
        if len(self):
            content = json.loads(self)
            for block in content['data']:
                template_name = 'sirtrevor/blocks/%s.html' % block['type']
                html.append(render_to_string(template_name, block['data']))
        return u''.join(html)


custom_blocks_registry = {}

def register_block(block, name=None):
    if name is None:
        name = block.name
    custom_blocks_registry[name] = block
