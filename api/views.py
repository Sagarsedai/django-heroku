from django.shortcuts import render
from .models import User
from .serializers import UserSerializer

from rest_framework import generics


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

from rest_framework import permissions

# authenticating JWTTokens in request payload headers
class JwtAuthorized(JWTAuthentication):
    def authenticate(self, request):
        try:
            auth_status = super().authenticate(request=request)
            return auth_status 
        except InvalidToken:
            return None

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JwtAuthorized]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JwtAuthorized]
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import json

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.username
        token['is_active']=user.is_active
        token['is_superuser']=user.is_superuser
        token['is_staff']=user.is_staff

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer