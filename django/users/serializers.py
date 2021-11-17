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
