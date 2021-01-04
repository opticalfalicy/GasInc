from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.

from projects.models import Project, ProjectImage
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3
@admin.register(Project)
class PersonAdmin(admin.ModelAdmin):
    pass
    inlines = [ProjectImageInline,]



# admin.site.register(Project, PersonAdmin)