from .models import Chat, Person
from .serializers import ChatSerializer, UserSerializer
from rest_framework import generics

class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class UserList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = UserSerializer
