from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import GetUserAppoinmentSerializer, SetUserAppoinmentSerializer,GetDoctorAppoinmentSerializer,SetDoctorAppoinmentSerializer
from .models import DoctorAppoinment, UserAppoinment
# Create your views here.

class SetUserAppoinmentView(APIView):
    def post(self,request,format=None):
        serializer = SetUserAppoinmentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'appoinment booked'},status=status.HTTP_200_OK)

class GetUserAppoinmentView(APIView):
    def get(self,request):
        appoinments = UserAppoinment.objects.all()
        serializer = GetUserAppoinmentSerializer(appoinments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class SetDoctorAppoinmentView(APIView):
    def post(self,request,format=None):
        serializer = SetDoctorAppoinmentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'data sent todoctor booked'},status=status.HTTP_200_OK)

class GetDoctorAppoinmentView(APIView): 
    def get(self,request):
        appoinments = DoctorAppoinment.objects.all()
        serializer = GetDoctorAppoinmentSerializer(appoinments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
