from django.apps import AppConfig
from watson import search as watson

class IssuesConfig(AppConfig):
    """
    Issue Configuration Class
    """
    name = 'issues'
    def ready(self):
        issue = self.get_model('Issue')
        watson.register(issue)
