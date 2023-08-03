from rest_framework import serializers
from .models import CustomUser, Post
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
       Сериалайзер для регистрации пользователей

       """
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ( 'email', 'username', 'password', )


class UserSerializer(serializers.ModelSerializer):
    """
       Сериалайзер для вывода пользователей

       """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', "password"]


class PostSerializer(serializers.ModelSerializer):
    """
       Сериалайзер для вывода постов

       """
    class Meta:
        model = Post
        fields = ['title', 'body', "user"]


