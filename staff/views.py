from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import GetDoctorsSerializer
from rest_framework.views import APIView
from .models import Doctor
# Create your views here.
class GetDoctorsView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()  # Retrieve all doctors
        serializer = GetDoctorsSerializer(doctors, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK) 