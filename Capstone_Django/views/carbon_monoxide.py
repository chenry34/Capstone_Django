from django.http import HttpResponse


def get_co_status(request):
    return HttpResponse("Temperature is 20 degrees")


def set_co_status(request):
    return HttpResponse("success")
