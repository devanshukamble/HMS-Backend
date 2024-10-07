from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import InsertContactUsSerializer
from .utils import Util
# Create your views here.
class InsertContactUsView(APIView):
    def post(self,request,format=None):
        serializer = InsertContactUsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'data inserted in contactus'},status=status.HTTP_200_OK)

class SendNewsletterEmailView(APIView):
    def post(self,request,format=None):
        print(request.data)
        data = { 
                'subject': 'Subscription Of Newsleter',
                'body': f'Thankyou for subscribeing MediManage newsleter',
                'to_email': request.data.get('email')
            }
        Util.send_email(data)
        return Response({'msg':'email sent'},status=status.HTTP_200_OK)