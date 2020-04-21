from django.urls import path
from main.views import *
urlpatterns = [
    path('<str:token>',Home, name='Home'),
    path('', Make, name = "Make new")
]