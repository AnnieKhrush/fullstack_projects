from django.urls import path
#from users.views import user_info, user_add_to_chat, delete_from_chat, page
from users.views import page, UserInfo

urlpatterns = [
    path('', page, name='page'),
    path('<user_id>/', UserInfo.as_view(), name='user_info'),
    #path('chat/add/<user_id>/<chat_id>/', user_add_to_chat, name='user_add_to_chat'),
    #path('chat/delete/<user_id>/<chat_id>/', delete_from_chat, name='delete_from_chat'),
]