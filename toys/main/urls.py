from django.urls import path, include
from .views import *
urlpatterns = [
    path('', start, name='default'),
    path('form/', forming, name='form'),
]