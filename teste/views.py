from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

class UserCreateView(APIView): 

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
           user = serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login_user(request):
    username = request.POST['username']
    password = request.POST['possword']
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        return Response([{'ok':1}])
    else:
        return Response([{'ok':2}])