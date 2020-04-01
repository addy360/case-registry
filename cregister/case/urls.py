from django.urls import path
from .views import case_form

urlpatterns = [
    path('', case_form, name='case' ),
]
