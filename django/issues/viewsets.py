from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from watson import search as watson
import json
from unidecode import unidecode

from comments.serializers import CommentarySerializer
from issues.serializers import IssueSerializer, IssueSearchFieldsSerializer
from issues.models import Issue, Vote
from rest_framework.pagination import PageNumberPagination

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
    def rate(self, request, slug=None):  # pylint:disable=unused-argument
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


    @action(detail=False, methods=['post'], name='Search similar issues',
            url_path='search', url_name='search')
    def search(self, request):  # pylint:disable=unused-argument
        """
        POST: Search query with a Issue, return list of similiar Issues
        """
        if request.method == 'POST':

            query_title = request.data['title']
            query_description = request.data['description']
            
            #Case two strings equals to ""
            # if (query_description == "" and query_title == ""):
            
            #get list of insignificant words and remove of query string
            stop_words_file = open('/app/issues/utils/stop-words.json')
            stop_words = json.load(stop_words_file)
            stop_words = stop_words['pt-br']
            
            query_words = query_title.split() + query_description.split()
            query_words = map(lambda x: unidecode(x.lower()), query_words)
            result_words  = [word for word in query_words if word not in stop_words]
            result_query = ' '.join(result_words)

            #transform Issues title/description strings in lowerCase and ASCII
            all_issues_parsed = Issue.objects.all().filter(visible=True)
            for issue in range(len(all_issues_parsed)):
                all_issues_parsed[issue].title = unidecode(all_issues_parsed[issue].title.lower())
                all_issues_parsed[issue].description = unidecode(all_issues_parsed[issue].description.lower())
            
            #get results
            print(result_query)
            # search_results = watson.search(result_query, ranking=True)

            search_results = watson.filter(all_issues_parsed, result_query, ranking=True)

            paginator = PageNumberPagination()
            page = paginator.paginate_queryset(search_results, request)
            serializer = IssueSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
            



    def get_serializer_class(self):
        if self.action == 'search':
            return IssueSearchFieldsSerializer
        return IssueSerializer
