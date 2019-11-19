from django.http import HttpResponse
from ..models import Door
import datetime


def get_door_status(request):
    door = Door.objects.last()
    if door.value == 0:
        return HttpResponse("Door is closed")
    else:
        return HttpResponse("Door is Open")


def set_door_status(request):
    door = Door(value=request.GET.get('door'), time_stamp=datetime.datetime.now())
    door.save()
    return HttpResponse("success")
