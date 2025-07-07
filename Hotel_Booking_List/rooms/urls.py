from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('room/new/', views.room_create, name='room_create'),
    path('room/<int:pk>/edit/', views.room_update, name='room_update'),
    path('room/<int:pk>/delete/', views.room_delete, name='room_delete'),
]
