from django.shortcuts import render
from .models import Chat, Person
from .serializers import ChatSerializer, PersonSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['sender', 'receiver']
    search_fields = ['value']
    #filter_backends = [filters.OrderingFilter]
    #ordering_fields = ['sender', 'receiver']
    ordering = ['-id']


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['username', 'email']
    search_fields = ['value']
    ordering = ['id']

