from django.contrib import admin

# Register your models here.
from uploader.models import UploadFile, Upload

admin.site.register(Upload)
admin.site.register(UploadFile)