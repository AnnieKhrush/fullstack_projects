from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from users.models import User
from chats.models import Chat

# Create your views here.
@require_http_methods(['GET'])
def user_info(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user = {
        'Имя пользователя (username)': user.username,
        'Имя': user.first_name,
        'Фамилия': user.last_name,
        'День рождения': user.date_of_birth,
        'Город': user.place_of_living,
        'Дополнительная информация': user.user_info,
    }
    return JsonResponse(user)


@require_http_methods(['PUT'])
def user_add_to_chat(request, user_id, chat_id):
    user = get_object_or_404(User, id=user_id)
    chat = get_object_or_404(Chat, id=chat_id)

    try:
        user_chat = User.objects.get(id=user_id, user_chats=chat)
        response = {
            'Пользователь': user.username,
            'Уже состоит в чате': chat.chat_title
        }
    except User.DoesNotExist:
        user.user_chats.add(chat)
        user.save()
        response = {
            'Пользователь': user.username,
            'Добавлен в чат': chat.chat_title
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
            'Пользователь': user.username,
            'Больше не состоит в чате': chat.chat_title
        }
    except User.DoesNotExist:
        response = {
            'Пользователь': user.username,
            'Не состоял в этом чате': chat.chat_title
        }        
    return JsonResponse(response)


@require_http_methods(['GET'])
def page(request):
    return render(request, 'start_page_users.html')
