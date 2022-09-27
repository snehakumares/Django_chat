from multiprocessing.sharedctypes import Value
from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'homepage.html')

def room(request, room):
    username = request.GET.get('username')
    roomdetails = Room.objects.get(name=room)
    return render(request, 'room.html', {'room':room,'room_details':roomdetails, 'username':username})

def check(request):
    roomname = request.POST['room_name']
    username = request.POST['username']
    if(Room.objects.filter(name=roomname).exists()):
        return redirect('/'+roomname+'/?username='+username)
    else:
        new_room = Room.objects.create(name=roomname)
        new_room.save()
        return redirect('/'+roomname+'/?username='+username)

def send(request):
    roomid = request.POST['room_id']
    username = request.POST['username']
    message = request.POST['message']
    new_message = Message.objects.create(roomid=roomid,username=username,value=message)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(roomid=room_details.id)
    return JsonResponse({"messages":list(messages.values())})