from django.conf import settings
from rest_framework import serializers

from .models import Logo
from .models import LogoImage

# M_V_L = settings.MAX_NAME_LENGTH

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['name', 'description', 'id']
    # def validate_name(self, value):
    #     if len(value) > M_V_L:
    #         raise forms.ValidationError("The value is too long")
    #     return value
    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoImage
        fields = ['image', 'a']