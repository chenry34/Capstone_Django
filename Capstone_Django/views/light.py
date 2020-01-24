from django.http import HttpResponse
from ..models import Light
from django.http import JsonResponse
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def get_light_status(request):
    date = datetime.today() - timedelta(days=1)
    light = Light.objects.filter(time_stamp__gte=date)
    return Response(light.values())


def set_light_status(request):
    value = request.GET.get('light')
    if value == "true":
        value = 1
    else:
        value = 0

    light = Light(value=value, time_stamp=datetime.now())
    light.save()
    return HttpResponse("success")

