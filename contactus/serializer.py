from rest_framework import serializers
from .models import ContactUs
class InsertContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['name','phoneno','email','message']
