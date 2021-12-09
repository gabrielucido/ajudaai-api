from rest_framework import serializers

from issues.models import Issue, Vote, IssueSearchFields


class IssueSerializer(serializers.ModelSerializer):
    """Issue Serializer."""

    upvotes = serializers.IntegerField(source='get_upvotes', read_only=True)
    downvotes = serializers.IntegerField(
        source='get_downvotes', read_only=True)
    vote = serializers.SerializerMethodField(read_only=True)

    def get_vote(self, obj):
        token = self.context.get('token', False)
        if token:
            vote = Vote.objects.filter(issue=obj, token=token)
            if vote.exists():
                return vote.first().upvote
        return None

    class Meta:
        """Serializer Options."""
        model = Issue
        fields = '__all__'

class IssueSearchFieldsSerializer(serializers.ModelSerializer):
    class Meta:
         model = IssueSearchFields
         fields = ['title', 'description', 'page']
