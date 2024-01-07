from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Player


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password = validated_data['password']  ,email = validated_data['email'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = '__all__'

    def get_username(self, obj):
        # Accessing the related User model's username field
        return obj.user.username if obj.user else None

    def get_email(self, obj):
        # Accessing the related User model's email field
        return obj.user.email if obj.user else None