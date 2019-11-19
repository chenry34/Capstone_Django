from django.http import HttpResponse
from ..models import User
import datetime


def create_user(request):
    user = User(user_name="chenry", password="password", created_date=datetime.datetime.now())
    user.save()
    return HttpResponse("Success")