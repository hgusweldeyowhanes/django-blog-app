from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'product'

urlpatterns = [
     
     path('', views.home, name='home'),
     path('room/login/', views.LoginPage, name='login'),
     path('room/register/', views.Register, name='register'),
     path('room/logout/', views.LogOut, name='logout'),
     path('room/<int:pk>/', views.room, name='room'),
     path('room/topics/', views.topicPage, name='topics'),
     path('room/activity/', views.activityPage, name='activity'),
     path('room/profile/<str:pk>/', views.userProfile, name = 'user-profile'),
     path('room/create-room/', views.createRoom, name='create-room'),
     path('room/update-room/<str:pk>/', views.updateRoom, name='update-room'),
     path('room/delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
     path('room/delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
     path('room/update-message/<str:pk>/', views.updateMessage, name='update-message'),
     path('room/user-update/', views.userUpdate, name='user-update'),
     path('room/poll/<int:poll_id>/', views.RoomPoll, name='poll'),
     path('room/poll/<int:poll_id>/vote', views.Vote_poll, name='vote_poll'),
     path('room/poll/create/', views.pollFormView, name='create_poll'),

     





]