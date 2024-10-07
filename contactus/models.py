from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()