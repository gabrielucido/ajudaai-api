from rest_framework import serializers

from animals.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    """Animal Serializer."""

    class Meta:
        """Serializer Options."""
        model = Animal
        fields = ['id', 'name', 'created_at', 'updated_at', 'description']
