from django.http import HttpResponse
from ..models import Light
from django.http import JsonResponse
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_light_status(request):
    light = Light.objects.last()
    return Response(light.value)


def set_light_status(request):
    light = Light(value=request.GET.get('light'), time_stamp=datetime.datetime.now())
    light.save()
    return HttpResponse("success")

