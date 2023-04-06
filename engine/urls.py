from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from engine import views

urlpatterns = [
    path('machines/', views.MachineList.as_view()),
    path('machines/<int:pk>/', views.MachineDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)