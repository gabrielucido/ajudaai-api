from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from reports.serializers import ReportSerializer
from reports.models import Report, Vote


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Reports.
    """

    @action(detail=True, methods=['post'], name='Report Rate',
            url_path='rate', url_name='rate')
    def rate(self, request, pk=None):  # pylint:disable=unused-argument
        """
        Upvote or Downvote a report.
        """
        report = self.get_object()
        upvote = request.data.get('upvote', None)
        if upvote == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        vote = Vote(report=report, upvote=upvote)
        vote.save()
        return Response(ReportSerializer(report).data, status=status.HTTP_200_OK)

    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Report.objects.all()
