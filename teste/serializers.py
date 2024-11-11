import re
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CadastroSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2", "first_name", "last_name"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'], 
            password=validated_data['password']
        )
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user
    
    #     email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{2,}$)"
    #     if not re.match(email_regex, email):
    #         raise serializers.ValidationError("Invalid email format.")
        
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
              return {'user': user}
            else:
                raise serializers.ValidationError('Invalid username or password')
        else: 
            raise serializers.ValidationError('Username and password are require.')
       
        return attrs
    