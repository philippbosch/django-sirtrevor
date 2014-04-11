django-sirtrevor
================

**django-sirtrevor** is a simple Django app that provides a content editing
widget based on the fantastic `Sir Trevor`_ project.


Quick start
-----------

1. Install django-sirtrevor::

    pip install django-sirtrevor

2. Add ``sirtrevor`` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'sirtrevor',
    )

3. Add sir trevor urls::

    url(r'^sirtrevor/', include('sirtrevor.urls')),

4. Create a model that makes use of ``SirTrevorField``::

    from django.db import models
    from sirtrevor.fields import SirTrevorField

    class MyModel(models.Model):
        ...
        content = SirTrevorField()
        ...

5. Now you can …

   - see it in action in the Django admin
   - create a ``ModelForm`` from your model
   - create a plain ``Form`` and use ``sirtrevor.forms.SirTrevorFormField``
   - use ``sirtrevor.widgets.SirTrevorWidget`` as a widget replacement for a
     ``Textarea``


Configuration
-------------

`Sir Trevor`_ has a few `configuration options`_. You can customize most of
them project-wide in your ``settings.py`` or some on a per-widget basis as
``kwargs`` for ``SirTrevorWidget``.


**Available options** (``CONFIGURATION_SETTINGS`` / ``widget_kwargs``):


``SIRTREVOR_BLOCK_TYPES`` / ``st_block_types``
    A list of block types to use with the editor.
    Defaults to ``['Text', 'List', 'Quote', 'Image', 'Video', 'Tweet', 'Heading']``

``SIRTREVOR_DEFAULT_TYPE`` / ``st_default_type``
    The default block to start the editor with.
    Defaults to ``None``

``SIRTREVOR_BLOCK_LIMIT`` / ``st_block_limit``
    The overall total number of blocks that can be displayed.
    Defaults to ``0``

``SIRTREVOR_BLOCK_TYPE_LIMITS`` / ``st_block_type_limits``
    Limit on the number of blocks that can be displayed by its type.
    Defaults to ``{}``

``SIRTREVOR_REQUIRED`` / ``st_required``
    Mandatory block types that are required for validatation.
    Defaults to ``None``

``SIRTREVOR_UPLOAD_URL`` / ``st_upload_url``
    URL for AJAX image uploads.
    Defaults to ``/sirtrevor/attachments/`` (depending on where you include
    django-sirtrevor's URLs in ``urls.py``)

``SIRTREVOR_UPLOAD_PATH``
    Path where to store uploaded images relative to ``MEDIA_ROOT``. (not
    configurable via widget kwargs)
    Defaults to ``attachments``

``SIRTREVOR_ATTACHMENT_PROCESSOR``
    A string containing a dotted path to a function that will be run before
    saving an uploaded image. See `below`_ for more details. (not configurable via
    widget kwargs)
    Defaults to ``None``


Resizing Images
---------------

You can resize uploaded images by implementing a function somewhere in your
code and pointing ``SIRTREVOR_ATTACHMENT_PROCESSOR`` to its location. The first
argument will be the file object and the method must return a
``SimpleUploadFile`` object.

Example implemented in ``utils.py`` in an app called ``core``.
``SIRTREVOR_ATTACHMENT_PROCESSOR`` set to ``core.utils.resize_attachment``::

    from PIL import Image
    from StringIO import StringIO
    from django.core.files.uploadedfile import SimpleUploadedFile


    def resize_attachment(file_):
        size = (1024, 9999)
        try:
            temp = StringIO()
            image = Image.open(file_)
            image.thumbnail(size, Image.ANTIALIAS)
            image.save(temp, 'jpeg')
            temp.seek(0)
            return SimpleUploadedFile(file_.name, temp.read(), content_type='image/jpeg')
        except Exception as ex:
            return file_


Custom Blocks
-------------

*Sir Trevor* can be extended through `custom blocks`_. Starting with 0.2.1
*django-sirtrevor* also has basic support for custom blocks.

Here is a little step-by-step guide:

**myapp/blocks.py**::

    from sirtrevor.blocks import BaseBlock

    class MyCustomBlock(BaseBlock):
        name = 'MyCustomName'

        class Media:
            js = ['sirtrevor/blocks/mycustomblock.js']


**myapp/models.py**::

    import sirtrevor
    from .blocks import MyCustomBlock

    sirtrevor.register_block(MyCustomBlock)


**myapp/static/sirtrevor/blocks/mycustomblock.js**::

    SirTrevor.Blocks.MyCustomName = SirTrevor.Block.extend({
        type: 'mycustomblock',
        // ...
    });

Please refer to *Sir Trevor*'s docs regarding `custom blocks`_ for details
about the JavaScript part of a custom block.


**myapp/templates/sirtrevor/blocks/mycustomblock.html**::

    <div class="content-block mycustom-block">
        <!-- Whatever JSON the custom block creates is available in the template -->
    </div>


**settings.py**::

    # ...

    SIRTREVOR_BLOCK_TYPES = ['Text', '...', 'MyCustomName']

    # ...


For reference please check out `django-sirtrevor-file`_ which implements a
simple block type for file downloads.



License
-------

MIT_


.. _Sir Trevor: http://madebymany.github.io/sir-trevor-js/
.. _MIT: http://philippbosch.mit-license.org/
.. _configuration options: http://madebymany.github.io/sir-trevor-js/docs.html#2
.. _key features: https://github.com/philippbosch/django-sirtrevor/issues/2
.. _below: #resizing-images
.. _custom blocks: http://madebymany.github.io/sir-trevor-js/docs.html#4
.. _django-sirtrevor-file: https://github.com/philippbosch/django-sirtrevor-file
