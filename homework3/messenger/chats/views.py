from http.client import HTTPResponse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def chat_list(request):
    if request.method == 'GET':
        chats = [
            {'id': 1, 'title': 'Personal chat'},
            {'id': 2, 'title': 'Private chat'},
            {'id': 3, 'title': 'Chat with cats'},
            {'id': 4, 'title': 'Chat for studying'}
        ]
        return JsonResponse({'chats': chats})
    else:
        return HttpResponse(status = 405)

def chat_title(request, pk):
    if request.method == 'GET':
        chats = [
            {'chat_id': 1, 'chat_title': 'Personal chat'},
            {'chat_id': 2, 'chat_title': 'Private chat'},
            {'chat_id': 3, 'chat_title': 'Chat with cats'},
            {'chat_id': 4, 'chat_title': 'Chat for studying'}
        ]
        return JsonResponse({'Name of a chat': chats[pk - 1]['chat_title']})
    else:
        return HttpResponse(status = 405)

@csrf_exempt
def create_chat(request):
    if request.method == 'POST':
        new_chat = [
            {'chat_id': request.POST, 'chat_title': request.POST}
        ]
        return JsonResponse({'New chat': new_chat})
    else:
        return HttpResponse(status = 405)