from rest_framework import serializers
from .models import Doctor

class GetDoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor 
        fields = ['firstname','lastname','email','dateofbirth','age','salary','joineddate','education', 'speciality', 'phonenumber', 'email','image']