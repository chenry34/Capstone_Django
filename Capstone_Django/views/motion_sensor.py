from django.http import HttpResponse
from ..models import Motion
from django.http import JsonResponse
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_motion_status(request):
    motion = Motion.objects.last()
    return Response(motion.value)


def set_motion_status(request):
    motion = Motion(value=request.GET.get('motion'), time_stamp=datetime.datetime.now())
    motion.save()
    return HttpResponse("success")

