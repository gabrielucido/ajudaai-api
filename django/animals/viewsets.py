from rest_framework import permissions, viewsets

from animals.serializers import AnimalSerializer
from animals.models import Animal


class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Animals.
    """

    serializer_class = AnimalSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Animal.objects.all()
