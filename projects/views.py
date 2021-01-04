import random 
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.utils.http import is_safe_url

# import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .forms import ProjectForm
from .models import Project
from .models import ProjectImage
from .serializers import ProjectSerializer
from .serializers import ImageSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# logger = logging.getLogger(__name__)

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


@api_view(['POST'])
def project_create_view(request, *args, **kwargs):
    # data = request.POST
    serializer = ProjectSerializer(data = request.POST)
    if serializer.is_valid(raise_exception = True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def project_detail_view(request, project_id, *args, **kwargs):
    qs = Project.objects.filter(id=project_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ProjectSerializer(obj)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def project_list_view(request, *args, **kwargs):
    qs = Project.objects.all()
    # qsi = ProjectImage.objects.all()
    print(qs)
    # qsi = qs.image.all()
    serializer = ProjectSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def project_image_view(request, *args, **kwargs):
    qsi = ProjectImage.objects.all()
    # qsi = ProjectImage.objects.all()
    print(qsi)
    # qsi = qs.image.all()
    serializer = ImageSerializer(qsi, many=True)
    return Response(serializer.data)



# def project_create_view_pure_django(request, *args, **kwargs):
#     form = ProjectForm(request.POST or None)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         # do other form related logic
#         obj.save()
#         form = ProjectForm()
#     return render(request, 'components/form.html', context={"form": form})

# def project_project_view(request, *args, **kwargs ):

#     obj = Project.objects.get(pk=2)
#     data = {

#         "main_tag": obj.main_tag,

#     }
#     status = 200
#     try:
#         status = 200 
#     except:

#         status = 404
#     return JsonResponse(data, status = 200)

# def project_id_view(request, project_id, *args, **kwargs):
#     print(args, kwargs)
#     # data = {
#     #     "id": project_id,
#     #     # "name": obj.name
#     # }
#     status = 200
#     try:
#         obj = Project.objects.get(id=project_id)
#         data['name'] = obj.name
#     except:
#         data['message'] = "Not Found"
#         status = 404
#     return JsonResponse(data, status=status)
   


# def project_category_view(request, *args, **kwargs):
#     print(args, kwargs)
#     # obj = Project.objects.get(pk=2)
#     data = {
#         # "id": project_id,
#     #     # "name": obj.name,

#     }
#     status = 200
#     try:
#         obj = Project.objects.get(pk = 1)
#         data['name'] = obj.name
#         data['main_tag'] = obj.main_tag
#         data['image'] = obj.image
#         data['tags'] = obj.tags
#     except:
#         status = 404
#     return JsonResponse(data, status = status)

# def project_list_view_pure_django(request, *args, **kwargs):
#     qs = Project.objects.all()
#     project_list = [x.serialize() for x in qs]
#     data = {
#         "response": project_list
#     }
#     return JsonResponse(data)



# def project_item_view(request, project_name, *args, **kwargs):
#     tags = Project.objects.get(pk=2)

#     return HttpResponse(tags.tags.all())


# def project_tags_view(request, project_tags, *args, **kwargs):
#     print(args, kwargs)
#     obj = Project.objects.get()
#     data = {



#         "tags": obj.tags.all()

#     }



  
#     return JsonResponse(data, status = 200)