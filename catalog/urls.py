from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('rooms/', views.RoomListView.as_view(), name='rooms'),
    path('room/<int:pk>', views.RoomDetailView.as_view(), name='room-detail'),
]