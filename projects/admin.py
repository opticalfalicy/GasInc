from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.

# from projects.models import Project, ProjectImage
from projects.models import Project
from projects.models import ProjectImage
# class ProjectImageInline(admin.TabularInline):
    # model = Project
    # extra = 3
# @admin.register(Project)
class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage
    # extra
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]
    
    class Meta:
        model = Project
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass        
# @admin.register(PersonAdmin)
# class PersonAdmin(admin.ModelAdmin):
#     pass
    # inlines = [ProjectImageInline,]



# admin.site.register(PersonAdmin)