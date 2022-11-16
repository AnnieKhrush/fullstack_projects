from django.urls import path
from chats.views import create_chat, create_message, chat_info, message_info, chat_list, message_list, chat_edit, message_edit, chat_delete, message_delete, message_check, page

urlpatterns = [
    path('create/', create_chat, name='create_chat'),
    path('message/create', create_message, name='create_message'),
    path('info/<chat_id>/', chat_info, name='chat_info'),
    path('message/info/<message_id>/', message_info, name='message_info'), 
    path('list/<user_id>/', chat_list, name='chat_list'),
    path('message/list/<user_id>/', message_list, name='message_list'),
    path('edit/<chat_id>/', chat_edit, name='chat_edit'),
    path('message/edit/<message_id>/', message_edit, name='message_edit'),
    path('delete/<chat_id>/', chat_delete, name='chat_delete'),
    path('message/delete/<message_id>/', message_delete, name='message_delete'),
    path('message/checked/<message_id>/', message_check, name='message_check'),
    path('', page, name='page'),
]