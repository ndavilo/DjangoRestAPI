from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

