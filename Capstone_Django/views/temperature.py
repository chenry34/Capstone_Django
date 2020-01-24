from django.http import HttpResponse
from ..models import Temperature
from django.http import JsonResponse
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_temperature(request):
    date = datetime.today() - timedelta(days=1)
    temp = Temperature.objects.filter(time_stamp__gte=date)
    return Response(temp.values())


def set_temperature(request):
    temp = Temperature(value=request.GET.get('temperature'), time_stamp=datetime.now())
    temp.save()
    return HttpResponse("success")