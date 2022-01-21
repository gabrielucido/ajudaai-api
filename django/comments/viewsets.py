from rest_framework import permissions, viewsets

from comments.serializers import CommentarySerializer
from comments.models import Commentary


class CommentaryViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    API endpoint to Comments.
    """

    serializer_class = CommentarySerializer
    permission_classes = [permissions.AllowAny]
    queryset = Commentary.objects.all()
