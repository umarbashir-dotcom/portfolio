from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
