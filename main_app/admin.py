from django.contrib import admin 
  
from .models import Flagged, UploadEmail 
admin.site.register(Flagged)
admin.site.register(UploadEmail)

