from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('start_work/', views.start_work, name='start_work'),
    path('start_break/', views.start_break, name='start_break'),
    path('end_break/', views.end_break, name='end_break'),
    path('end_work/', views.end_work, name='end_work'),
    path('test/', views.actually_worked_hours, name='test'),
]