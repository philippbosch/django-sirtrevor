import os
import json
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import AttachmentForm
from .conf import settings

AUTH_TEST = lambda u: u.is_staff
UPLOAD_PATH = settings.SIRTREVOR_UPLOAD_PATH


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
        name = os.path.join(UPLOAD_PATH, safe_name)
        path = default_storage.save(name, file_)
        url = default_storage.url(path)
        return HttpResponse(json.dumps({'file': {'url': url, 'filename': path}}))
    else:
        return HttpResponse('Error')
