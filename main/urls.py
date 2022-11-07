from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='index'),
    path('login', login),
    path('signup', signup),
]