from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class UserAppoinment(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=10)
    email = models.EmailField()
    doctorname = models.CharField(max_length=255)
    timeslot = models.DateTimeField()
    symptoms = models.TextField()
    def clean(self):
        super().clean()
        now = timezone.now()
        one_week_later = now + timedelta(weeks=1)
        if not (now <= self.timeslot <= one_week_later):
            raise ValidationError(f"Appointment date must be within one week from now. Current time: {now}, Range: {now} to {one_week_later}")
    # def __str__(self):
    #     return f"{self.email} | {self.doctorname}"

class DoctorAppoinment(models.Model):
    doctorname = models.CharField(max_length=255)
    timeslot = models.DateTimeField()
    # def __str__(self) -> str:
    #     return f"{self.doctorname} | {self.timeslot}"