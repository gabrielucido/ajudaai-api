from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from comments.serializers import CommentarySerializer
from issues.serializers import IssueSerializer
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

    def create(self, request):
        """
        Create a Issue
        """
        data = request.data
        if "image" in data:
            issue = Issue.objects.create(title=data['title'],
                                         description=data['description'],
                                         image=data['imageSrc'])
        else:
            issue = Issue.objects.create(title=data['title'],
                                         description=data['description'])
        issue.save()
        serializer = IssueSerializer(issue)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
    lookup_field = 'slug'
