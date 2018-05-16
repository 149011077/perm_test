from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Student)

@admin.register(models.Permission)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('describe','name', 'url', 'per_method', 'argument_list')
    list_per_page = 20
    ordering = ('-id',)