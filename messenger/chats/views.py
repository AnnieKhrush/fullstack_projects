from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
import json
from chats.models import Chat, Message
from users.models import User

# Create your views here.
@require_http_methods(['POST'])
def create_chat(request):
    new_chat = Chat.objects.create(chat_title=request.POST.get('chat_title'), chat_description=request.POST.get('chat_description'))
    new_chat.save()
    users = request.POST.getlist('users')
    for user_id in users:
        user = get_object_or_404(User, id=int(user_id))
        user.save()
        user.user_chats.add(new_chat)
        user.save()
    response = {
        'Заголовок нового чата': new_chat.chat_title,
        'Описание нового чата': new_chat.chat_description
    }
    return JsonResponse(response)


@require_http_methods(['POST'])
def create_message(request):
    chat_id = request.POST.get('chat_id')
    chat = get_object_or_404(Chat, id=chat_id)
    text = request.POST.get('new_message')
    new_message = Message.objects.create(message=text, message_in_chat=chat)
    new_message.save()
    response = {
        'Текст нового сообщения': new_message.message,
        'Новое сообщение находится в чате': new_message.message_in_chat.chat_title
    }
    return JsonResponse(response)



@require_http_methods(['GET'])
def chat_info(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    chat = {
        'Заголовок': chat.chat_title,
        'Описание чата': chat.chat_description,
        'Дата создания чата': chat.chat_created_at
    }
    return JsonResponse(chat)


@require_http_methods(['GET'])
def message_info(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message = {
        'Чат, к которому относится сообщение': message.message_in_chat.chat_title,
        'Текст сообщения': message.message,
        'Время создания сообщения': message.message_created_at
    }
    return JsonResponse(message)


@require_http_methods(['GET'])
def chat_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    chats = user.user_chats.all()
    chat_list = []
    for chat in chats:
        chat_list.append({
            'Заголовок': chat.chat_title,
            'Описание чата': chat.chat_description,
            'Дата создания чата': chat.chat_created_at
        })
    return JsonResponse({'Список чатов': chat_list})


@require_http_methods(['GET'])
def message_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    chats = user.user_chats.all()
    messages_list = []
    for chat in chats:
        messages = Message.objects.filter(message_in_chat=chat)
        for message in messages:
            messages_list.append({
                'Чат, к которому относится сообщение': message.message_in_chat.chat_title,
                'Текст сообщения': message.message,
                'Время создания сообщения': message.message_created_at
            })
    return JsonResponse({'Список сообщений': messages_list})


@require_http_methods(['PUT'])
def chat_edit(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    new_data = json.loads(request.body)
    chat.chat_title = new_data.get('chat_title')
    chat.chat_description = new_data.get('chat_description')
    chat.save()
    response = {
        'Заголовок измененного чата': chat.chat_title,
        'Описание измененного чата': chat.chat_description,
        'Дата создания чата': chat.chat_created_at
    }
    return JsonResponse(response)


@require_http_methods(['PUT'])
def message_edit(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.message = json.loads(request.body).get('message')
    message.save()
    response = {
        'Чат, к которому относится изменённое сообщение': message.message_in_chat.chat_title,
        'Текст изменённого сообщения': message.message,
        'Время создания сообщения': message.message_created_at
    }
    return JsonResponse(response)


@require_http_methods(['DELETE'])
def chat_delete(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    title = chat.chat_title
    chat.delete()
    return JsonResponse({'Удалённый чат': title})


@require_http_methods(['DELETE'])
def message_delete(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    text = message.message
    chat = message.message_in_chat.chat_title
    message.delete()
    response = {
        'Удалённое сообщение': text,
        'Сообщение принадлежало чату': chat
    }
    return JsonResponse(response)


@require_http_methods(['PUT'])
def message_check(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.checked = True
    message.save()
    response = {
        'Данное сообщение прочитано': message.message
    }
    return JsonResponse(response)


def page(request):
    if request.method == 'GET':
        return render(request, 'start_page_chats.html')
    else:
        return HttpResponse(status=405)