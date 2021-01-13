from django.conf import settings
from rest_framework import serializers

from .models import Project
from .models import ProjectImage

# M_V_L = settings.MAX_NAME_LENGTH

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['model', 'make', 'image', 'id']
    # def validate_name(self, value):
    #     if len(value) > M_V_L:
    #         raise forms.ValidationError("The value is too long")
    #     return value
    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['project', 'images']