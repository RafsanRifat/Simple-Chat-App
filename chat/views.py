from django.shortcuts import render


# Create your views here.
from chat.models import Message


def lobby(request):
    return render(request, 'chat/lobby.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})
