from django.urls import path
from chats.views import chat_list, chat_title, create_chat

urlpatterns = [ 
    path('chats_list', chat_list, name='chat_list'),
    path('title/<int:pk>/', chat_title, name='chat_title'),
    path('create_a_chat/', create_chat, name='create_chat')
]