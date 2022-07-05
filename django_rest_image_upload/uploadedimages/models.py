import os.path
import uuid
from PIL import Image

from django.db import models
# from django.contrib.auth.models import User, Group
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill
# from imagekit.cachefiles import ImageCacheFile
from django.conf import settings


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


class UserImage(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField("Uploaded`Image", upload_to=custom_filename)
    # thumbnail = ImageSpecField(source='image',
    #                            processors=[ResizeToFill(200, 200)],
    #                            format=get_image_extension,
    #                            options={'quality': 70})
    thumbnail = models.ImageField("Thumbnail of Image", blank=True)

    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):
        self.thumbnail = create_thumbnail(self.image)
        super(UserImage, self).save(force_update=force_update)

    def __str__(self):
        return self.title
