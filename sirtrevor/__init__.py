import json
from django.template.loader import render_to_string
from django.utils.encoding import python_2_unicode_compatible
import six


#@python_2_unicode_compatible
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

    def get_blocks(self, type=None):
        if not len(self):
            return
        _blocks = json.loads(self)['data']

        return [block for block in _blocks if not type or block['type'] is type or block['type'] in type]


    def get_first_block(self, type=None):
        try:
            return self.get_blocks(type)[0]
        except IndexError:
            return None

    #def __str__(self):
    #    for block in self.get_blocks():
    #        text = block['data'].get('text', False)
    #        if text:
    #            return text


custom_blocks_registry = {}


def register_block(block, name=None):
    if name is None:
        name = block.name
    custom_blocks_registry[name] = block
