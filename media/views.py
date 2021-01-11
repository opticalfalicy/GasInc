from django.shortcuts import render

# Create your views here.

import random 
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.utils.http import is_safe_url

# import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .forms import ProjectForm
from .models import Image
from .models import Logo
from .serializers import LogoSerializer
from .serializers import ImageSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# logger = logging.getLogger(__name__)

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


@api_view(['POST'])
def logo_create_view(request, *args, **kwargs):
    # data = request.POST
    serializer = LogoSerializer(data = request.POST)
    if serializer.is_valid(raise_exception = True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def logo_detail_view(request, logo_id, *args, **kwargs):
    qs = Logo.objects.filter(id=logo_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = LogoSerializer(obj)
    return Response(serializer.data, status=200)


# @api_view(['GET'])
# def project_list_view(request, *args, **kwargs):
#     qs = Project.objects.all()
#     # qsi = ProjectImage.objects.all()
#     print(qs)
#     # qsi = qs.image.all()
#     serializer = ProjectSerializer(qs, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def logo_image_view(request, *args, **kwargs):
    qsi = LogoImage.objects.all()
    # qsi = ProjectImage.objects.all()
    print(qsi)
    # qsi = qs.image.all()
    serializer = ImageSerializer(qsi, many=True)
    return Response(serializer.data)
