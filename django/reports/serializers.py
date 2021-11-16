from rest_framework import serializers

from reports.models import Report, Vote


class ReportSerializer(serializers.ModelSerializer):
    """Report Serializer."""

    upvotes = serializers.IntegerField(source='get_upvotes', read_only=True)
    downvotes = serializers.IntegerField(
        source='get_downvotes', read_only=True)
    vote = serializers.SerializerMethodField(read_only=True)

    def get_vote(self, obj):
        token = self.context.get('token', False)
        if token:
            vote = Vote.objects.filter(report=obj, token=token)
            if vote.exists():
                return vote.first().upvote
        return None

    class Meta:
        """Serializer Options."""
        model = Report
        fields = '__all__'
