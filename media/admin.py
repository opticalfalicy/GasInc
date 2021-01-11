from django.contrib import admin

# Register your models here.

from media.models import Logo, LogoImage
class LogoImageInline(admin.TabularInline):
    model = LogoImage
@admin.register(Logo)
class PersonAdmin(admin.ModelAdmin):
    pass
    inlines = [LogoImageInline,]
