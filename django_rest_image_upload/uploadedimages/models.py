from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField("Uploaded Image")

    def __str__(self):
        return self.title
