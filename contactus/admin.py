from django.contrib import admin
from .models import ContactUs

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id','name','phoneno','email','message']

admin.site.register(ContactUs,ContactUsAdmin)