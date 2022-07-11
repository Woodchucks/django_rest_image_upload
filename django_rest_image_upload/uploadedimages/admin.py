from django.contrib import admin
from .models import UploadImage, UserProfile, Plan


admin.site.register(UploadImage)
admin.site.register(UserProfile)
admin.site.register(Plan)
