from tokenize import TokenError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ChangePasswordSerializer, SendResetPasswordEmailSerializer, UserLoginSerializer, UserPasswordRestSerializer, UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate,login,logout
from account.renderer import UserRenderer
from rest_framework.permissions import IsAuthenticated
# for generating tokens manually we use the below function
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class UserRegistrationView(APIView):
    # below line is used to use the custome error renderer we made for our benifit
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data = request.data)
        
        serializer.is_valid(raise_exception=True) 
        
        user = serializer.save()
        # token = get_tokens_for_user(user)
        return Response({'msg':'Registration Success'},status=status.HTTP_201_CREATED)
        
class UserLoginView(APIView):
    # below line is used to use the custome error renderer we made for our benifit
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data = request.data)
        
        serializer.is_valid(raise_exception = True) 
        
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        print(email,password)
        user = authenticate(email = email, password = password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'login successful'},status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'errors':{
                        'non_field_errors':['email or password is not valid']
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        print(request)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = ChangePasswordSerializer(data = request.data,context = {'user':request.user})
        
        serializer.is_valid(raise_exception=True)
        
        return Response({'msg':'password changed'},status=status.HTTP_200_OK)
    
class SendResetPasswordEmailView(APIView):
    def post(self,request,format=None):
        serializer = SendResetPasswordEmailSerializer(data = request.data)
        
        serializer.is_valid(raise_exception=True)
                
        return Response({'msg':'password reset link send to your email'},status=status.HTTP_200_OK)
    
class UserPasswordRestView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer = UserPasswordRestSerializer(data = request.data,context={'uid':uid,'token':token})
        
        serializer.is_valid(raise_exception=True)
        
        return Response({'msg':'password reset successfully'},status=status.HTTP_200_OK)

class TokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        try:
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)
            return Response({'access': new_access_token}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'errors': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)