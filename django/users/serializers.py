from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer.
    """
    class Meta:
        """User Serializer Options."""
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'username', 'email']

class CreateAnonUserSerializer(serializers.ModelSerializer):
    """
    Create anon user and return id and auth token.
    """
    token = serializers.CharField(read_only=True)
    username = serializers.CharField(write_only=True)
    class Meta:
        """CreateAnonUserSerializer Options."""
        model = get_user_model()
        fields = ['username', 'token']
        write_only_fields = ['username']
    
    def get_token(self, obj):
        """
        Get token and return it.
        """
        return obj.token.key
        