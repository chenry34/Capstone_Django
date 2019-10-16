from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import User
import datetime


def index(request):
    return HttpResponse("Testing a simple request")


# Example of how temperature request will look
def get_temperature(request):
    return HttpResponse("Temperature is 20 degrees")


def create_user(request):
    user = User(user_name="chenry", password="password", created_date=datetime.datetime.now())
    user.save()
    return HttpResponse("Success")

