# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import CadastroSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class CadastroView(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = CadastroSerializer
    
    def create(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # token, create = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        # 'token': token.key, 
        return Response({serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
       
    

class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer
    
class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'hellor':"Bem Vindo"})
    