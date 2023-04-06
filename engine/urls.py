from django.urls import path
from engine import views

urlpatterns = [
    path('machines/', views.machine_list),
    path('machines/<int:pk>/', views.machine_detail),
]