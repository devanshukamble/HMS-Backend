from xml.dom import ValidationErr
from django.forms import ValidationError
from rest_framework import serializers
from .models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util


class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this because we need to confirm the password
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', "firstname", "lastname", "dateofbirth", "gender", "address1",
                  "address2", "city", "state", "country", "zipcode", 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # validate password and password2

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError({
                'non_field_errors': {'password': 'password and confirm password do not match'}
            }
            )
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    # this is requried because the email from frontend is needed to store to compare
    email = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', "firstname", "lastname", "dateofbirth",
                  "gender", "address1", "address2", "city", "state", "country", "zipcode"]


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        newPassword = attrs.get('password')
        newPassword2 = attrs.get('password2')
        user = self.context.get('user')
        if newPassword != newPassword2:
            raise serializers.ValidationError(
                {'password': 'password and confirm password do not match'})
        user.set_password(newPassword)
        user.save()
        return attrs


class SendResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('encoded uid', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('password token', token)
            link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token+'/'
            print('Password reset link ', link)
            # send the link to email
            data = { 
                'subject': 'Reset Password',
                'body': f'Please click on the link to reset your password {link}',
                'to_email': user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise ValidationErr('you are not a registered user')


class UserPasswordRestSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            newPassword = attrs.get('password')
            newPassword2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if newPassword != newPassword2:
                raise serializers.ValidationError(
                    {'password': 'password and confirm password do not match'})
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError(
                    'token is invalid or expired')
            user.set_password(newPassword)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('Token is not Valid or Expired')
