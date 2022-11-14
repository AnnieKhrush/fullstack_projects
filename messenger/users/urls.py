from django.urls import path
from users.views import user_info, user_add_to_chat, delete_from_chat, page

urlpatterns = [
    path('', page, name='page'),
    path('<user_id>/', user_info, name='user_info'),
    path('add_to_chat/<user_id>/<chat_id>/', user_add_to_chat, name='user_add_to_chat'),
    path('delete_from_chat/<user_id>/<chat_id>/', delete_from_chat, name='delete_from_chat'),
]