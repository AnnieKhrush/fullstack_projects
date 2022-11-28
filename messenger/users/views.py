from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from users.models import User
from chats.models import Chat
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from users.serializers import UserSerializer, UserAddDeleteSerializer

# Create your views here.
class UserInfo(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

    def get_object(self):
        user_id = self.kwargs['user_id']
        return get_object_or_404(User, id=user_id)


class UserAddDelete(RetrieveUpdateAPIView):
    serializer_class = UserAddDeleteSerializer
    queryset = User.objects.all()

    def get_object(self):
        user_id = self.kwargs['user_id']
        chat_id = self.kwargs['chat_id']
        user = get_object_or_404(User, id=user_id)
        chat = get_object_or_404(Chat, id=chat_id)
        try:
            users_chat = User.objects.get(id=user_id, user_chats=chat)
        except User.DoesNotExist:
            user.user_chats.add(chat)
        return 0
'''
@require_http_methods(['GET'])
def user_info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_of_birth': user.date_of_birth,
        'place_of_living': user.place_of_living,
        'additional_info': user.user_info,
    }
    return JsonResponse(user)
'''

@require_http_methods(['PUT'])
def user_add_to_chat(request, user_id, chat_id):
    user = get_object_or_404(User, id=user_id)
    chat = get_object_or_404(Chat, id=chat_id)

    try:
        user_chat = User.objects.get(id=user_id, user_chats=chat)
        response = {
            'user': user.username,
            'already_in_chat': chat.chat_title
        }
    except User.DoesNotExist:
        user.user_chats.add(chat)
        user.save()
        response = {
            'user': user.username,
            'added_to_chat': chat.chat_title
        }        
    return JsonResponse(response)


@require_http_methods(['DELETE'])
def delete_from_chat(request, user_id, chat_id):
    user = get_object_or_404(User, id=user_id)
    chat = get_object_or_404(Chat, id=chat_id)
    try:
        check_user = User.objects.get(id=user_id, user_chats=chat)
        check_chat = check_user.user_chats.get(id=chat_id)
        check_user.user_chats.remove(check_chat)
        response = {
            'user': user.username,
            'not_in_chat': chat.chat_title
        }
    except User.DoesNotExist:
        response = {
            'user': user.username,
            'not_from_chat': chat.chat_title
        }        
    return JsonResponse(response)


@require_http_methods(['GET'])
def page(request):
    return render(request, 'start_page_users.html')
