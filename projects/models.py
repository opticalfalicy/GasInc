import os
from django.db import models
from django.conf import settings
import random

# from taggit.managers import TaggableManager
# from tagging.registry import register

# Create your models here.

# def images_path():
#     return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Project(models.Model):
    name = models.CharField(max_length=100)
    main_tag = models.CharField(max_length=100)
    # tags = TaggableManager()
    # image = models.CharField(max_length=100000000000)
    # image = models.FileField(upload_to='images/', blank = True, null = True )
    # image = models.FileField(upload_to='images/')
    # posted_on = models.DateTimeField(auto_now_add=True)
    # started_at = models.DateTimeField(auto_now_add=False)
    # finished_at = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.main_tag}, {self.name}"

    def serialize(self): 
        return{
            "id": self.id,
            "name": self.name,
            "main_tag": self.main_tag,
            # "images": self.images
            # "likes": random.randint(0, 229)
        }

# class NewProject(models.Model)

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    a = Project.name

    def serialize(self):
        return{
            "image": self.image, 
            "a": self.a
        }