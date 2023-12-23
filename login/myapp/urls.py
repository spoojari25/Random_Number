# myapp/urls.py
from django.urls import path
from .views import dashboard, get_latest_random_number

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('get_latest_random_number/', get_latest_random_number, name='get_latest_random_number'),
]
