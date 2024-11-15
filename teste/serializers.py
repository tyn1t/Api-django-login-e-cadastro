from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class CadastroSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]
        extra_kwargs  = {'password': {'write_only':True}}
    
    def create(self, validated_data):
        # remove password2
        validated_data.pop('confirm_password')
        # valita password 
        password = validated_data.pop(password)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('senha erro')
        return data 
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
               refresh = RefreshToken.for_user(user)
               data['refresh'] = str(refresh)
               data['access'] = str(refresh.access_token)
            else:
                raise serializers.ValidationError('Login inválido. Verifique suas credenciais.')
        else:
            raise serializers.ValidationError('Informe o nome de usuário e a senha.')
        return data
                     


