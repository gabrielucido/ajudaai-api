from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from watson import search as watson

from comments.serializers import CommentarySerializer
from issues.serializers import IssueSerializer, IssueSearchFieldsSerializer
from issues.models import Issue, Vote


class IssueViewSet(viewsets.ModelViewSet):
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
    def rate(self, request, pk=None):  # pylint:disable=unused-argument
        """
        Upvote or Downvote a issue.
        """
        issue = self.get_object()
        upvote = request.data.get__name__('upvote', None)
        token = request.data.get('token', None)
        if upvote == None or token == None:
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
    def comments(self, request, pk=None):  # pylint:disable=unused-argument
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

    @action(detail=False, methods=['post'], name='Search similar issues',
            url_path='search', url_name='search')
    def search(self, request):  # pylint:disable=unused-argument
        """
        POST search query with a Issue, return list of similiar Issues
        """
        if request.method == 'POST':
            title = request.data['title']
            description = request.data['description']
            query = title + ' ' + description
            # to do: remove insignificant words for search


            search_results = watson.filter(Issue.objects.all(),query)
            return Response(IssueSerializer(search_results, many=True).data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if self.action == 'search':
            return IssueSearchFieldsSerializer
        return IssueSerializer
