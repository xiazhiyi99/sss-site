from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('submit/<int:rank_id>', views.submit_page, name='submit_page'),
    path('<int:rank_id>', views.rank_page, name='rank_page'),
]