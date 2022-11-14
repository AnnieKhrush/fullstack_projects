from django.db import models
from django.utils import timezone

# Create your models here.
class Chat(models.Model):
    chat_title = models.CharField(max_length=32, verbose_name='Название чата')
    chat_description = models.TextField(null=True, verbose_name='Описание чата', blank=True)
    chat_created_at = models.DateTimeField(null=True, default=timezone.now, verbose_name='Дата создания чата')

    def __str__(self):
        return self.chat_title

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ('-chat_created_at',)


class Message(models.Model):
    message = models.TextField(max_length=256, verbose_name='Текст сообщения')
    message_created_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания сообщения')
    message_in_chat = models.ForeignKey(Chat, null=True, on_delete=models.CASCADE, related_name='chat_messages',  verbose_name='Чат, к которому относится сообщение')
    checked=models.BooleanField(default=False,verbose_name='Сообщение прочитано/нет')

    def __str__(self):
        return f'{self.message} {self.message_created_at}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('-message_created_at',)
