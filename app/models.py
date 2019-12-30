import os, random
from django.db import models


def get_filename_ext(filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 234324343221)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'img/{new_filename}/{final_filename}'


class Message(models.Model):
    name = models.CharField(max_length=200, unique=True)
    text = models.CharField(max_length=1000)
    password = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.name
