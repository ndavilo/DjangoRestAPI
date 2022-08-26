from django.db import models
from django.utils import timezone

class Person(models.Model):
    username    = models.CharField(max_length=100)
    email       = models.EmailField()
    password    = models.CharField(max_length=100)

class Chat(models.Model):
    sender      = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='senders')        
    receiver    = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='receivers')        
    value       = models.CharField(max_length=1000000)
    timestamp   = models.DateTimeField(auto_now_add=True)
    is_read     = models.BooleanField(default=False)
    def __str__(self):
        return self.value
    class Meta:
        ordering = ('timestamp',)