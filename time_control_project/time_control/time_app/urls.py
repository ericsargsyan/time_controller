from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('start_work/', views.start_work, name='start_work'),
    path('end_work/', views.end_work, name='end_work'),
]