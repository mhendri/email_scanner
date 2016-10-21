from django.db import models

class Priviledged(models.Model):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    email = models.EmailField()
    upload = models.FileField(upload_to= 'uploads/')
