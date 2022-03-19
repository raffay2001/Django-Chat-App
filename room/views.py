from django.shortcuts import render
from .models import Message, Room
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login/')
def rooms(request):
    rooms = Room.objects.all()
    context = {
        'rooms' : rooms
    }
    return render(request, 'room/rooms.html', context)


@login_required(login_url='login/')
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    context = {
        'room' : room,
        'messages':messages,
    }
    return render(request, 'room/room.html', context)

