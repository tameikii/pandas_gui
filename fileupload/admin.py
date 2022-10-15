from django.contrib import admin
from .models import Category, FileList, FileUploader
# Register your models here.
admin.site.register(Category)
admin.site.register(FileList)
admin.site.register(FileUploader)
