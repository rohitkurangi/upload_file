from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.core.login import UserTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer