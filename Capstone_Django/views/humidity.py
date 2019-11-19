from django.http import HttpResponse


def get_humidity(request):
    return HttpResponse("Temperature is 20 degrees")


def set_humidity(request):
    return HttpResponse("success")
