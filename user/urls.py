from django.urls import path
from .views import index

urlpatterns = [
    path('user', index, name='index'),
]