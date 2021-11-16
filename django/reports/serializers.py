from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    """Report Serializer."""

    upvotes = serializers.IntegerField(source='get_upvotes', read_only=True)
    downvotes = serializers.IntegerField(source='get_downvotes', read_only=True)

    class Meta:
        """Serializer Options."""
        model = Report
        fields = '__all__'
