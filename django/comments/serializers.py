from rest_framework import serializers

from comments.models import Commentary


class CommentarySerializer(serializers.ModelSerializer):
    """Commentary Serializer."""

    class Meta:
        """Serializer Options."""
        model = Commentary
        fields = '__all__'
