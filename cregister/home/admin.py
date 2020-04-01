from django.contrib import admin

from .models import ClientIssues, CaseType

admin.site.register(ClientIssues)
admin.site.register(CaseType)