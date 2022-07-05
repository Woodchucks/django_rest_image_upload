import uuid
import os.path
from PIL import Image
from datetime import time

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import User, Group


def custom_filename(image, filename):
    image_extension = get_image_extension(image, filename)
    return '{}.{}'.format(uuid.uuid4(), image_extension)


def get_image_extension(image, filename):
    return filename.split(".")[-1]


def get_image_basename(image, filename):
    filename_split_arr = filename.split(".")
    basename = "".join(filename_split_arr[0])
    return basename


def create_thumbnail(uploaded_image, size=(200, 200,)):
    if not uploaded_image or uploaded_image == "":
        return None

    image = Image.open(uploaded_image)
    image.thumbnail(size, Image.ANTIALIAS)
    filename = custom_filename(None, os.path.basename(uploaded_image.name))
    basename = get_image_basename(uploaded_image, filename)
    extension = get_image_extension(uploaded_image, filename)
    new_filename = "thumb_{}.{}".format(basename, extension)
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename


def create_binary_image(uploaded_image):
    image = Image.open(uploaded_image)
    image = image.convert('1')
    filename = custom_filename(None, os.path.basename(uploaded_image.name))
    basename = get_image_basename(uploaded_image, filename)
    extension = get_image_extension(uploaded_image, filename)
    new_filename = "binary_{}.{}".format(basename, extension)
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename


# search for 'dynamic links' in google, django-dynamic-link - PyPI
# def link_expired(self):
#     time_img_was_uploaded = self.time_from_image_upload
#     time_now = time.time()
#     difference = time_now - time_img_was_uploaded
#     if difference > self.time_link_expires:
#         self.binary_img = None


class UploadImage(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField("Uploaded Image", upload_to=custom_filename)
    thumbnail = models.ImageField("Thumbnail of Image", blank=True)
    binary_img = models.ImageField("Binary Image", blank=True)
    time_link_expires = models.IntegerField("Time to link expires", null=True,
                                            validators=[MinValueValidator(300),
                                                        MaxValueValidator(30000)])
    time_from_image_upload = models.TimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):
        self.thumbnail = create_thumbnail(self.image)
        self.binary_img = create_binary_image(self.image)
        super(UploadImage, self).save(force_update=force_update)

    def __str__(self):
        return self.title
