from django.db import models
from chats.models import Chat
from datetime import date

# Create your models here.
class User(models.Model):
    username = models.CharField(unique=True, max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateField(null=True, default=date.fromisoformat('2000-03-03'))
    user_info = models.TextField(null=True)
    user_chat = models.ManyToManyField(Chat)
