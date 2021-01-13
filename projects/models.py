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
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    # tags = TaggableManager()
    # image = models.CharField(max_length=100000000000)
    # image = models.FileField(upload_to='images/', blank = True, null = True )
    # image = models.FileField(upload_to='images/')
    # posted_on = models.DateTimeField(auto_now_add=True)
    # started_at = models.DateTimeField(auto_now_add=False)
    # finished_at = models.DateTimeField(auto_now_add=False)
    image = models.FileField(blank=True)

    def __str__(self):
        return f"{self.make}, {self.model}"

    def serialize(self): 
        return{
            "id": self.id,
            "model": self.model,
            "make": self.make,
            "image": self.image
            # "likes": random.randint(0, 229)
        }

# class NewProject(models.Model)

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    # print(Project)
    images = models.FileField(upload_to = "images/")
    # pId = Project.id

    # def __str__(self):
    #     return self.project.id

    def serialize(self):
        return{
            "project": self.project,
            "images": self.images, 
            # "pId": self.pId,
            # "a": self.a
        }