from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.TextField(max_length=256)
    message_created_at = models.DateTimeField()

class Chat(models.Model):
    chat_title = models.CharField(max_length=32)
    chat_created_at = models.DateTimeField()
    chat_message = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL)
