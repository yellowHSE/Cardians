from django.urls import path
from .views import *
from django.conf.urls import include


urlpatterns = [
    path('mycar', mycar),
    path('animation_car', animation_car),
    #, include('webpush.urls')),
]