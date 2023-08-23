# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from chat.models import Room

@login_required(login_url='/login')
def index(request):
    return render(request, 'chat/index.html')

@login_required(login_url='/login')
def room(request, room_name):
    room, created = Room.objects.get_or_create(id=room_name)
    # messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chat/room.html", {
        'room_name': room_name,
        # 'messages': messages,
    })
