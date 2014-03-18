django-sirtrevor
================

**django-sirtrevor** is a simple Django app that provides a content editing
widget based on the fantastic `Sir Trevor`_ project.

~~~~

**IMPORTANT:** This package should be considered (pre-)alpha. It is by no
means feature-complete or bug-free. It is a work-in-progress and right now
lacks some `key features`_.

~~~~


Quick start
-----------

1. Install django-sirtrevor::

    pip install django-sirtrevor

2. Add `sirtrevor` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'sirtrevor',
    )

3. Add sir trevor urls
    
    url(r'', include('sirtrevor.urls')),

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
   - use ``sirtrevor.widgets.SirTrevorWidget`` as a widget replacement for a ``Textarea``


Configuration
-------------

`Sir Trevor` has a few `configuration options`_. You can customize most of them 
project-wide in your ``settings.py`` or on a per-widget basis as ``kwargs`` for 
``SirTrevorWidget``.

**Available options** (``CONFIGURATION_SETTINGS`` / ``widget_kwargs``):


``SIRTREVOR_BLOCK_TYPES`` / ``st_block_types``
    Specify an array of block types to use with the editor.
    Defaults to ``['Text', 'List', 'Quote', 'Image', 'Video', 'Tweet', 'Heading']``

``SIRTREVOR_DEFAULT_TYPE`` / ``st_default_type``
    Specify a default block to start the editor with.
    Defaults to ``None``

``SIRTREVOR_BLOCK_LIMIT`` / ``st_block_limit``
    Set an overall total number of blocks that can be displayed.
    Defaults to ``0``

``SIRTREVOR_BLOCK_TYPE_LIMITS`` / ``st_block_type_limits``
    Set a limit on the number of blocks that can be displayed by its type.
    Defaults to ``{}``

``SIRTREVOR_REQUIRED`` / ``st_required``
    Specify which block types are required for validatation.
    Defaults to ``None``

``SIRTREVOR_UPLOAD_URL`` / ``st_upload_url``
    Specify url for AJAX image uploads.
    Defaults to ``attachments``

``SIRTREVOR_UPLOAD_PATH``
    Specify where to upload images to within media path (not configurable via widget kwargs).
    Defaults to ``attachments``

License
-------

MIT_


.. _Sir Trevor: http://madebymany.github.io/sir-trevor-js/
.. _MIT: http://philippbosch.mit-license.org/
.. _configuration options: http://madebymany.github.io/sir-trevor-js/docs.html#2
.. _key features: https://github.com/philippbosch/django-sirtrevor/issues/2
