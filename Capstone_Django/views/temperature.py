from django.http import HttpResponse


# Example of how temperature request will look
def get_temperature(request):
    return HttpResponse("Temperature is 20 degrees")


def set_temperature(request):
    return HttpResponse("success")
