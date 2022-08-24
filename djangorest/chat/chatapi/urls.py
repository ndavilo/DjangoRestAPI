from django.contrib import admin
from django.urls import path
from .views import message_list, message_detail, users_view, user_view

urlpatterns = [
    path('message/', message_list),
    path('message/<int:pk>', message_detail),
    path('user/', users_view),
    path('user/<int:pk>', user_view),
]