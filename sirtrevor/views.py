import importlib
import json
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from PIL import Image
from .forms import AttachmentForm


AUTH_TEST = lambda u: u.is_staff


@csrf_exempt
@require_POST
@user_passes_test(AUTH_TEST)
def attachment(request):
    #remap sirtrevors filename
    request.FILES['attachment'] = request.FILES['attachment[file]']
    form = AttachmentForm(request.POST, request.FILES)
    if form.is_valid():
        file_ = form.cleaned_data['attachment']
        image_types = ['image/png', 'image/jpg', 'image/jpeg', 'image/pjpeg', 'image/gif']
        if file_.content_type not in image_types:
            return HttpResponse(status=403, content='Bad image format')
        file_name, extension = os.path.splitext(file_.name)
        safe_name = '{0}{1}'.format(slugify(file_name), extension)
        name = os.path.join(settings.SIRTREVOR_UPLOAD_PATH, safe_name)

        if settings.SIRTREVOR_ATTACHMENT_PROCESSOR is not None:
            if callable(settings.SIRTREVOR_ATTACHMENT_PROCESSOR):
                processor = settings.SIRTREVOR_ATTACHMENT_PROCESSOR
            else:
                module, func = settings.SIRTREVOR_ATTACHMENT_PROCESSOR.rsplit('.', 1)
                processor = getattr(importlib.import_module(module), func)
            file_ = processor(file_)

        try:
            size = Image.open(file_).size
        except:
            size = None

        path = default_storage.save(name, file_)
        url = default_storage.url(path)
        return HttpResponse(json.dumps({'file': {'url': url, 'filename': path, 'size': size}}))
    else:
        return HttpResponse('Error')
