from django.http import HttpResponse
from ..models import Motion
from django.http import JsonResponse
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_motion_status(request):
    date = datetime.today() - timedelta(days=1)
    motion = Motion.objects.filter(time_stamp__gte=date)
    return Response(motion.values())


def set_motion_status(request):
    motion = Motion(value=request.GET.get('motion'), time_stamp=datetime.now())
    motion.save()
    return HttpResponse("success")

