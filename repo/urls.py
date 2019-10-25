from django.contrib import admin
from django.urls import include,path,re_path
from .views import *

urlpatterns = [
    path('', repo, name='repo'),
    path('<int:file_id>/', download, name='download'),
    path('<int:file_id>/remove/', remove, name='remove'),
]