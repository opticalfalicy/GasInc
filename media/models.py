import os
from django.db import models
from django.conf import settings
import random

# from taggit.managers import TaggableManager
# from tagging.registry import register

# Create your models here.

# def images_path():
#     return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Logo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.description}, {self.name}"

    def serialize(self): 
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


class LogoImage(models.Model):
    logo = models.ForeignKey(Logo, related_name='logos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="logos")

    def serialize(self):
        return{
            "image": self.image, 
        }