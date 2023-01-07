from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.filters import BaseFilterBackend
# import json
from chats.models import Chat, Message
from users.models import User
from chats.serializers import ChatCreateSerializer, ChatChangeSerializer, ChatListSerializer, MessageChangeSerializer, MessageCreateSerializer, MessageListSerializer
from application.decorator import login_needed

# Create your views here.
@login_needed
def home_page(request):
    return render(request, 'home_page.html')
    

def login(request):
    return render(request, 'login.html')


# def index(request):
#     return render(request, 'index.html')


class ChatCreate(CreateAPIView):

    serializer_class = ChatCreateSerializer
    queryset = Chat.objects.all()
    lookup_field = 'id'


    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()


class ChatChange(RetrieveUpdateDestroyAPIView):

    serializer_class = ChatChangeSerializer
    queryset = Chat.objects.all()
    lookup_field = 'id'


    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()


class ChatList(viewsets.ViewSet):

    def list(self, request):
        user_id = request.user.id
        print(user_id)
        chats = Chat.objects.filter(chat_users=request.user)
        print(chats)
        return Response({'chats': ChatListSerializer(chats, many=True).data})



class MessageCreate(CreateAPIView):

    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()


class MessageChange(RetrieveUpdateDestroyAPIView):

    serializer_class = MessageChangeSerializer
    queryset = Message.objects.all()
    lookup_field = 'id'


    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()


class MessageList(ListAPIView):

    serializer_class = MessageListSerializer
    queryset = Message.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, id=chat_id)
        messages = Message.objects.filter(message_in_chat=chat)
        return messages


'''
@require_http_methods(['POST'])
def create_chat(request):
        chat_title=request.POST.get('chat_title')
        chat_description=request.POST.get('chat_description')
        
        users_id = request.POST.getlist('users')
        if chat_title == '' or chat_description == '':
            return JsonResponse({'Ошибка:': 'Название чата или его описание не могут быть пустыми'}, status=400)
        else:
            new_chat = Chat.objects.create(chat_title=chat_title, chat_description=chat_description)
            users = get_list_or_404(User, id__in=users_id)
            if len(users) != len(users_id):
                raise Http404
            for user in users:
                user.user_chats.add(new_chat)
            response = {
                'title_of_new_chat': new_chat.chat_title,
                'description_of_new_chat': new_chat.chat_description
            }
            return JsonResponse(response)


@require_http_methods(['POST'])
def create_message(request):
    chat_id = request.POST.get('chat_id')
    chat = get_object_or_404(Chat, id=chat_id)
    text = request.POST.get('new_message')
    new_message = Message.objects.create(message=text, message_in_chat=chat)
    response = {
        'new_message_text': new_message.message,
        'in_chat': new_message.message_in_chat.chat_title
    }
    return JsonResponse(response)


@require_http_methods(['GET'])
def chat_info(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    chat = {
        'title': chat.chat_title,
        'chat_description': chat.chat_description,
        'created_at': chat.chat_created_at
    }
    return JsonResponse(chat)


@require_http_methods(['GET'])
def message_info(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message = {
        'in_chat': message.message_in_chat.chat_title,
        'message_text': message.message
    }
    return JsonResponse(message)


@require_http_methods(['GET'])
def chat_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    chats = user.user_chats.all()
    chat_list = []
    for chat in chats:
        chat_list.append({
            'title': chat.chat_title,
            'chat_description': chat.chat_description
        })
    return JsonResponse({'Список чатов': chat_list})


@require_http_methods(['GET'])
def message_list(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(message_in_chat=chat)
    messages_list = []
    for message in messages:
        messages_list.append({
            'in_chat': message.message_in_chat.chat_title,
            'message_text': message.message
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
        'title_of_modified_chat': chat.chat_title,
        'description_of_modified_chat': chat.chat_description
    }
    return JsonResponse(response)


@require_http_methods(['PUT'])
def message_edit(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.message = json.loads(request.body).get('message')
    message.save()
    response = {
        'in_chat': message.message_in_chat.chat_title,
        'text_of_modified_chat': message.message
    }
    return JsonResponse(response)


@require_http_methods(['DELETE'])
def chat_delete(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    title = chat.chat_title
    chat.delete()
    return JsonResponse({'title_of_deleted_chat': title})


@require_http_methods(['DELETE'])
def message_delete(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    text = message.message
    chat = message.message_in_chat.chat_title
    message.delete()
    response = {
        'deleted_message': text,
        'from_chat': chat
    }
    return JsonResponse(response)


@require_http_methods(['PUT'])
def message_check(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.checked = True
    message.save()
    response = {
        'message_text': message.message,
        'checked': message.checked
    }
    return JsonResponse(response)




'''
