from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Testing a simple request")


# Example of how temperature request will look
def get_temperature(request):
    return HttpResponse("Temperature is 20 degrees")
