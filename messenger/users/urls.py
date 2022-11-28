from django.urls import path
#from users.views import user_info, user_add_to_chat, delete_from_chat, page
from users.views import UserInfo, UserAdd, UserDelete

urlpatterns = [
    path('<int:user_id>/', UserInfo.as_view(), name='user_info'),
    path('chat/add/<int:user_id>/', UserAdd.as_view(), name='user_add_to_chat'),
    path('chat/delete/<int:user_id>/', UserDelete.as_view(), name='delete_from_chat'),
]