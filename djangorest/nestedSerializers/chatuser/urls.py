from django.contrib import admin
from django.urls import path
from .views import ChatList, ChatDetails, UserList, UserDetails

urlpatterns = [
    path('chat/', ChatList.as_view()),
    path('chat/<int:pk>', ChatDetails.as_view()),
    path('person/', UserList.as_view()),
    path('person/<int:pk>', UserDetails.as_view()),
]