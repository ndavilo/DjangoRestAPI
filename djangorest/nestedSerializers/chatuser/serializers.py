from rest_framework import serializers
from .models import Chat, Person

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    senders =  ChatSerializer(read_only=True, many=True)
    receivers =  ChatSerializer(read_only=True, many=True)
    class Meta:
        model = Person
        fields = '__all__'