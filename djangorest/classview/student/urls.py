from django.contrib import admin
from django.urls import path
from .views import StudentList, StudentDetails

urlpatterns = [
    path('student/', StudentList.as_view()),
    path('student/<int:pk>', StudentDetails.as_view()),
]