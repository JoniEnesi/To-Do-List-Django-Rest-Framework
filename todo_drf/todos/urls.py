from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('home/', views.list, name='list'),
]