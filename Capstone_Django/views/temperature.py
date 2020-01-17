from django.http import HttpResponse
from ..models import Temperature
from django.http import JsonResponse
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_temperature(request):
    temp = Temperature.objects.last()
    return Response(temp.value)


def set_temperature(request):
    temp = Temperature(value=request.GET.get('temperature'), time_stamp=datetime.datetime.now())
    temp.save()
    return HttpResponse("success")