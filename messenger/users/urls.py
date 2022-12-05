from django.urls import path
#from users.views import user_info, user_add_to_chat, delete_from_chat, page
from users.views import UserInfo, UserAdd, UserDelete
from application.decorator import login_needed

urlpatterns = [
    path('<int:id>/', login_needed(UserInfo.as_view()), name='user_info'),
    path('chat/add/<int:id>/', login_needed(UserAdd.as_view()), name='user_add_to_chat'),
    path('chat/delete/<int:id>/', login_needed(UserDelete.as_view()), name='delete_from_chat'),
]