from django.contrib import admin
from django.urls import path
from .views import MessageList, MessageDetails, UserList, UserDetails

urlpatterns = [
    path('message/', MessageList.as_view()),
    path('message/<int:pk>', MessageDetails.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetails.as_view()),
]