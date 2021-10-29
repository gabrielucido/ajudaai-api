from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    """Report Serializer."""

    class Meta:
        """Serializer Options."""
        model = Report
        fields = ['id', 'name', 'created_at', 'updated_at', 'description']
