from django.db import models
from chats.models import Chat
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=32, verbose_name='Имя пользователя (username)')
    first_name = models.CharField(max_length=32, verbose_name='Имя')
    last_name = models.CharField(max_length=32, verbose_name='Фамилия')
    date_of_birth = models.DateField(null=True, default=date.fromisoformat('2000-03-03'), blank=True, verbose_name='Дата рождения')
    place_of_living = models.CharField(null=True, max_length=32, blank=True, verbose_name='Город')
    user_info = models.TextField(null=True, blank=True, verbose_name='Дополнительная информация')
    user_chats = models.ManyToManyField(Chat, related_name='user_chats', blank=True, verbose_name='Чаты пользователя')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'