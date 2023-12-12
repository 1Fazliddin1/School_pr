from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import AboutSchool, Documents, InternalDocs
# Register your models here.


@admin.register(AboutSchool)
class InfosAdmin(ModelAdmin):
    list_display = ['id', 'school_name_uz']
    # list_filter = []


@admin.register(Documents)
class DocumentsAdmin(ModelAdmin):
    list_display = ['id', 'doc_title_uz', 'doc_type', 'org_type', 'doc_code']
    list_filter = ['doc_type', 'org_type']
    search_fields = ['doc_title_uz', 'doc_title_ru', 'doc_title_en',]


@admin.register(InternalDocs)
class DocumentsAdmin(ModelAdmin):
    list_display = ['id', 'doc_title_uz', 'doc_type', 'doc_code']
    list_filter = ['doc_type']
    search_fields = ['doc_title_uz', 'doc_title_ru', 'doc_title_en',]