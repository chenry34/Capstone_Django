from django.http import HttpResponse
from ..models import Door
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_door_status(request):
    date = datetime.today() - timedelta(days=1)
    door = Door.objects.filter(time_stamp__gte=date)
    return Response(door.values())


def set_door_status(request):
    door = Door(value=request.GET.get('door'), time_stamp=datetime.now())
    door.save()
    return HttpResponse("success")
