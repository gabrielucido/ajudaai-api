from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from reports.serializers import ReportSerializer
from reports.models import Report


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Reports.
    """

    @action(detail=True, methods=['post'], name='Report Rate',
            url_path='rate', url_name='rate')
    def rate(self, request, pk=None):  # pylint:disable=unused-argument
        """
        Increment or decrement a report relevance.
        """
        report = self.get_object()
        increment = request.data.get('increment', None)
        if increment == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if increment:
            report.relevance += 15
        else:
            report.relevance -= 15
        report.save()
        return Response(ReportSerializer(report).data, status=status.HTTP_200_OK)

    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Report.objects.all()
