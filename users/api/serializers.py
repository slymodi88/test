import jwt as jwt
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from Ecommerce import settings
from users.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'token')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        user_created_token = User.objects.create_token(user)
        return user_created_token

    # def create(self, validated_data):
    #     password = validated_data.pop("password")
    #     hashed_password = make_password(password)
    #     user = User.objects.create(password=hashed_password, **validated_data)
    #     # user_created_token = create_token(users)
    #     # return user_created_token
    #     return user


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'token')
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'users not found'
            )
        return user
