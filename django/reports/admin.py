from django.contrib import admin

from reports.models import Report, Vote


admin.site.register(Report)
admin.site.register(Vote)
