from django.urls import path
from .views import client_form

urlpatterns = [
    path('', client_form, name='client' ),
]
