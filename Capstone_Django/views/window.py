from django.http import HttpResponse


def get_window_status(request):
    return HttpResponse("Temperature is 20 degrees")


def set_window_status(request):
    return HttpResponse("success")
