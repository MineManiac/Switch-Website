from rest_framework import serializers
from .models import User, Friend_Request


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'friends']

class UserFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['friends']

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class FriendRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend_Request
        fields = ['id', 'from_user']