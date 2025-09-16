from rest_framework import serializers
from apps.login.models import *


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = CustomUser
        fields = '__all__'
    