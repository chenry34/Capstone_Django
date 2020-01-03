from django.http import HttpResponse
from ..models import Window
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_window_status(request):
    window = Window.objects.last()
    if window.value == 0:
        return Response("Closed")
    else:
        return Response("Open")


def set_window_status(request):
    window = Window(value=request.GET.get('window'), time_stamp=datetime.datetime.now())
    window.save()
    return HttpResponse("success")
