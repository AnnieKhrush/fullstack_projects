from django.contrib import admin

# Register your models here.
from chats.models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_title', 'chat_description')
    search_fields = ('chat_title',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'message_in_chat', 'message_created_at', 'checked')
    search_fields = ('message_in_chat',)

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)