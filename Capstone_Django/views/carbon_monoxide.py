from django.http import HttpResponse
from ..models import CarbonMonoxide
from django.http import JsonResponse
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_co_status(request):
    date = datetime.today() - timedelta(days=1)
    co = CarbonMonoxide.objects.filter(time_stamp__gte=date)
    return Response(co.values())


def set_co_status(request):
    co = CarbonMonoxide(value=request.GET.get('co'), time_stamp=datetime.now())
    co.save()
    return HttpResponse("success")
