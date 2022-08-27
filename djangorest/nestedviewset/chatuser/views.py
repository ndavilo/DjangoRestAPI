from django.shortcuts import render
from .models import Chat, Person
from .serializers import ChatSerializer, PersonSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'receiver']


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']

