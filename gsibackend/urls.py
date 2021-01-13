"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


# from projects.views import home_view, project_project_view, project_category_view, project_tags_view, project_item_view

from django.conf.urls.static import static
from django.conf import settings 

from .views import index
from projects.views import home_view, project_list_view, project_image_view
# from projects.views import home_view, project_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('create-project/', project_create_view),
    path('projects/', project_list_view),
    path('images/',  project_image_view),
    # path('projects/<int:project_id>', project_id_view),
    # path('projects/<int:project_id>', project_list_view),
    # path('projects/<str:project_maintag>/', project_category_view),
    # path('projects/<str:project_tags>', project_tags_view),
    # path('projects/<str:project_maintag>/<str:project_name>', project_item_view),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)