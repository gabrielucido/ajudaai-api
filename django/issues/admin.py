from django.contrib import admin

from issues.models import Issue, Vote


admin.site.register(Issue)
admin.site.register(Vote)
