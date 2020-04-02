from django.urls import path
from .views import index, issue, caseType

urlpatterns = [
    path('', index, name='home' ),
    path('issue', issue, name='issue' ),
    path('caseType', caseType, name='caseType' ),
]
