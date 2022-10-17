from django.urls import path
from chats.views import chat_list, chat_info, create_chat, page

urlpatterns = [ 
    path('chats_list/', chat_list, name='chat_list'),
    path('<chat_id>/', chat_info, name='chat_info'),
    path('create_chat/', create_chat, name='create_chat'),
    path('', page, name='page'),
]