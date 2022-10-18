from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    message = models.TextField(max_length=256)
    message_created_at = models.DateTimeField(null=True, default=timezone.now)

class Chat(models.Model):
    chat_title = models.CharField(max_length=32)
    chat_description = models.TextField(null=True)
    chat_created_at = models.DateTimeField(null=True, default=timezone.now)
    chat_message = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL)
