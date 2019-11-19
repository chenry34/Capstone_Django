from django.http import HttpResponse


def get_motion_status(request):
    return HttpResponse("Temperature is 20 degrees")


def set_motion_status(request):
    return HttpResponse("success")
