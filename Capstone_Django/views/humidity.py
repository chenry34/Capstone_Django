from django.http import HttpResponse
from ..models import Humidity
from django.http import JsonResponse
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_humidity(request):
    humidity = Humidity.objects.last()
    return Response(humidity.value)


def set_humidity(request):
    humidity = Humidity(value=request.GET.get('humidity'), time_stamp=datetime.datetime.now())
    humidity.save()
    return HttpResponse("success")
