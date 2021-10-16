from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('register/',views.registerView,name='register'),

    path('',views.home,name='home'),
    path('room/<str:pkey>/',views.room,name='room'),

    path('profile/<str:pkey>',views.userProfile,name='user-profile'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pkey>/',views.updateRoom,name='update-room'),
    path('delete-room/<str:pkey>/',views.deleteRoom,name='delete-room'),
    path('delete-message/<str:pkey>/',views.deleteMessage,name='delete-message'),
    path('update-user/',views.updateUser,name='update-user'),
    path('topics/',views.topicPage,name='topics'),
]

