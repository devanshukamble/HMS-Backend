from rest_framework import serializers
from .models import UserAppoinment , DoctorAppoinment

class SetUserAppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAppoinment
        fields = "__all__"

class GetUserAppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAppoinment
        fields = ['firstname','lastname','phoneno','email','doctorname','timeslot','symptoms']

class SetDoctorAppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppoinment
        fields = "__all__"
class GetDoctorAppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppoinment
        fields = ['doctorname','timeslot']