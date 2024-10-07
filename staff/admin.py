from django.contrib import admin
from django.utils.html import format_html
from .models import Doctor
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','firstname', 'lastname', 'email', 'phonenumber', 'education', 'joineddate', 'salary', 'age', 'photo_tag')

    def photo_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: 50px;" />')
        return "No Image"
    photo_tag.short_description = 'Photo'
admin.site.register(Doctor,DoctorAdmin)