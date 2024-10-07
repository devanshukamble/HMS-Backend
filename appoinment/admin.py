from django.contrib import admin
from .models import UserAppoinment,DoctorAppoinment
# Register your models here.
class UserAppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'phoneno', 'email', 'doctorname', 'timeslot', 'symptoms')  # Add 'id' to the list

class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','doctorname', 'timeslot')  # Add 'id' to the list

admin.site.register(UserAppoinment,UserAppointmentAdmin)
admin.site.register(DoctorAppoinment,DoctorAppointmentAdmin)