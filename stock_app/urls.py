from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_list, name='phone_list'),
    path('add/', views.phone_create, name='phone_create'),
    path('edit/<int:pk>/', views.phone_update, name='phone_update'),
    path('delete/<int:pk>/', views.phone_delete, name='phone_delete'),
]
