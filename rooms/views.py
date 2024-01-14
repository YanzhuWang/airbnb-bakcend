from django.shortcuts import render
from django.http import HttpResponse

from rooms.models import Room


# Create your views here.
def see_all_rooms(request):
    rooms = Room.objects.all()
    for room in rooms:
        return HttpResponse(room.price)


def see_one_room(request, room_id, room_name):
    return HttpResponse(f"see one room with id: {room_id} -> {room_name}")
