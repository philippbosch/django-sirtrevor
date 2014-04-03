from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.functional import curry


def resize_image_attachment(file_, size=(1024, 9999)):
    try:
        temp = BytesIO()
        image = Image.open(file_)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(temp, 'jpeg')
        temp.seek(0)
        return SimpleUploadedFile(file_.name, temp.read(), content_type='image/jpeg')
    except Exception as ex:
        return file_


def resize_image_attachment_processor(w, h):
    return curry(resize_image_attachment, size=(w,h))
