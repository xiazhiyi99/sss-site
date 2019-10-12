from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home_page', views.index, name = 'home_page'),
]