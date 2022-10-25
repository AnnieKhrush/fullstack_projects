from django.db import models
from django.utils import timezone

# Create your models here.
class Chat(models.Model):
    chat_title = models.CharField(max_length=32)
    chat_description = models.TextField(null=True)
    chat_created_at = models.DateTimeField(null=True, default=timezone.now)


class Message(models.Model):
    message = models.TextField(max_length=256)
    message_created_at = models.DateTimeField(null=True, default=timezone.now)
    message_in_chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
