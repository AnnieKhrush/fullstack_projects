from django.urls import path
#from chats.views import create_chat, create_message, chat_info, message_info, chat_list, message_list, chat_edit, message_edit, chat_delete, message_delete, message_check, page 
from chats.views import ChatChange, ChatCreate, MessageChange, MessageCreate, ChatList, MessageList
from application.decorator import login_needed

urlpatterns = [
    path('create/', (ChatCreate.as_view()), name='create_chat'),
    path('<int:id>/', (ChatChange.as_view()), name='chat_info'),
    path('list/<int:user_id>/', (ChatList.as_view()), name='chat_list'),
    path('message/create/', (MessageCreate.as_view()), name='message_create'),
    path('message/<int:id>/', (MessageChange.as_view()), name='message_info'), 
    path('message/list/<int:chat_id>/', (MessageList.as_view()), name='message_list'),
    # path('index/', index, name='index'),
]