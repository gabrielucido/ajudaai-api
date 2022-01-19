from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters

from comments.serializers import CommentarySerializer
from issues.serializers import IssueSerializer
from issues.models import Issue, Vote


class IssueFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains", label="Titulo da Issue")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains", label="Descrição")
    start_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="gt", label="Data de inicio")
    end_date = filters.DateTimeFilter(field_name="created_at", lookup_expr="lt", label="Data final")

    class Meta:
        model = Issue
        fields = ['title', 'description', 'start_date', 'end_date']

 
class IssueViewSet(viewsets.ModelViewSet):  # pylint:disable=too-many-ancestors
    """
    API endpoint to Issues.
    """

    def get_serializer_context(self):
        context = super().get_serializer_context()
        token = self.request.GET.get('token', False)
        if self.request.data.get('token', False):
            token = self.request.data.get('token')
        context.update({'token': token}) 
        return context
        
    @action(detail=True, methods=['post'], name='Issue Rate',
            url_path='rate', url_name='rate')
    def rate(self, request, slug=None):  # pylint:disable=unused-argument
        """
        Upvote or Downvote a issue.
        """
        issue = self.get_object()
        upvote = request.data.get('upvote', None)
        token = request.data.get('token', None)
        if upvote is None or token is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            vote = Vote.objects.get(issue=issue, token=token)
            if vote.upvote == upvote:
                vote.delete()
            else:
                vote.upvote = upvote
                vote.save()
        except Vote.DoesNotExist:
            vote = Vote(issue=issue, upvote=upvote, token=token)
            vote.save()
        return Response(IssueSerializer(issue, context=self.get_serializer_context()).data,
                        status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], name='Issue Comments',
            url_path='comments', url_name='comments')
    def comments(self, request, slug=None):  # pylint:disable=unused-argument
        """
        Get comments of a issue.
        """
        issue = self.get_object()
        comments = issue.comments.filter(visible=True)
        return Response(CommentarySerializer(comments, many=True).data,
                        status=status.HTTP_200_OK)

    serializer_class = IssueSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Issue.objects.all()
    ilter_backends = (filters.DjangoFilterBackend,)
    filterset_class = IssueFilter
    lookup_field = 'slug'
