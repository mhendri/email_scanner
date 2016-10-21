from django.db import models
from django.contrib import admin

#class Priviledged(models.Model):
#    firstName = models.CharField(max_length = 200)
#    lastName = models.CharField(max_length = 200)
#    email = models.EmailField()
#    upload = models.FileField(upload_to= 'uploads/', null = True, blank = True)

class UploadEmail(models.Model):
    email_To = models.EmailField()
    email_From= models.EmailField()

class Flagged(models.Model):
    email_To =  models.EmailField()
    email_From =  models.EmailField()
    subject = models.CharField(max_length = 200)
    body = models.TextField()
    reason = models.TextField()
 
#class UploadEmails(admin.ModelAdmin):
#    list_display = ('email_To', 'email_From')

#class Flagged(admin.ModelAdmin):
#    list_display = ('email_To', 'email_From', 'body', 'reason')
