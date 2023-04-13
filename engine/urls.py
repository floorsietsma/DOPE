from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from engine import views

urlpatterns = [
    path('machines/', views.MachineList.as_view()),
    path('machines/<int:pk>/', views.MachineDetail.as_view()),
    path('factories/', views.FactoryList.as_view()),
    path('factories/<int:pk>/', views.FactoryDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('linesteps/', views.LineStepList.as_view()),
    path('linesteps/<int:pk>/', views.LineStepDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)