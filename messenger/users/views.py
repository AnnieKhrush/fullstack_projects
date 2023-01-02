from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from users.models import User
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from users.serializers import UserInfoSerializer, UserAddSerializer, UserDeleteSerializer

# Create your views here.
class UserInfo(RetrieveAPIView):

    serializer_class = UserInfoSerializer
    queryset = User.objects.all()
    lookup_field = 'id'



class UserAdd(UpdateAPIView):

    serializer_class = UserAddSerializer
    queryset = User.objects.filter()
    lookup_field = 'id'
    



class UserDelete(UpdateAPIView):

    serializer_class = UserDeleteSerializer
    queryset = User.objects.filter()
    lookup_field = 'id'

    


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
'''
