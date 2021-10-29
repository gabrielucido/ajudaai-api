from rest_framework import permissions, viewsets

from reports.serializers import ReportSerializer
from reports.models import Report


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Reports.
    """

    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Report.objects.all()
