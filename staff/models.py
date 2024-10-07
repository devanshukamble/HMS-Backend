from django.db import models

# Create your models here.
class Doctor(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    dateofbirth = models.DateField()
    age = models.PositiveIntegerField()
    salary = models.PositiveIntegerField()
    joineddate = models.DateField()
    education = models.CharField(max_length=255)
    speciality = models.CharField(max_length=100)
    image = models.ImageField(upload_to="doctor/images")
    def __str__(self):
        return f"{self.firstname} {self.lastname}"