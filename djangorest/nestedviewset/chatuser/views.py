from django.shortcuts import render
from .models import Chat, Person
from .serializers import ChatSerializer, PersonSerializer
from rest_framework import viewsets

class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

