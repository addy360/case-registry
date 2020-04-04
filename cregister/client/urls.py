from django.urls import path
from .views import client_form, client_details

urlpatterns = [
    path('', client_form, name='client' ),
    path('<int:id>', client_details, name='client_details')
]
