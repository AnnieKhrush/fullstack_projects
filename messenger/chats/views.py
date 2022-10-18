from http.client import HTTPResponse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
def chat_list(request):
    if request.method == 'GET':
        chats = {
            'chat_1':'Private chat',
            'chat_2':'Family chat',
            'chat_3':'Chat with cats',
            'chat_4':'Chat for studying'
        }
        return JsonResponse(chats)
    else:
        return HttpResponse(status=405)


def chat_info(request, chat_id):
    if request.method == 'GET':
        chats = [
            {'chat_id': 1, 'chat_title': 'Private chat', 'chat_description': 'Этот чат содержит личные данные', 'date_of_creation':'10.10.2022', 'last_message_time': '13:00 12.10.2022'},
            {'chat_id': 2, 'chat_title': 'Family chat', 'chat_description': 'Чат с семьей', 'date_of_creation':'07.08.2022', 'last_message_time': '22:45 17.10.2022'},
            {'chat_id': 3, 'chat_title': 'Chat with cats', 'chat_description': 'В этом чате обмениваемся фото котов', 'date_of_creation':'22.09.2022', 'last_message_time': '10:57 18.10.2022'},
            {'chat_id': 4, 'chat_title': 'Chat for studying', 'chat_description': 'Делимся информацией по учёбе', 'date_of_creation':'01.09.2022', 'last_message_time': '00:09 18.10.2022'}
        ]
        return JsonResponse(chats[int(chat_id) - 1])
    else:
        return HttpResponse(status=405)


def create_chat(request):
    if request.method == 'POST':
        new_chat = {
            'chat': request.POST
        }
        return JsonResponse(new_chat)
    else:
        return HttpResponse(status=405)
        

def page(request):
    if request.method == 'GET':
        return render(request, 'start_page_chats.html')
    else:
        return HttpResponse(status=405)