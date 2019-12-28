from django.http import HttpResponse
from ..models import Door
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_door_status(request):
    door = Door.objects.last()
    if door.value == 0:
        return Response("Closed")
    else:
        return Response("Open")


def set_door_status(request):
    door = Door(value=request.GET.get('door'), time_stamp=datetime.datetime.now())
    door.save()
    return HttpResponse("success")
