from django.http import HttpResponse
from ..models import Window
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_window_status(request):
    date = datetime.today() - timedelta(days=1)
    window = Window.objects.filter(time_stamp__gte=date)
    return Response(window.values())


def set_window_status(request):
    window = Window(value=request.GET.get('window'), time_stamp=datetime.now())
    window.save()
    return HttpResponse("success")
