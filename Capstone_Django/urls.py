from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getTemperature', views.get_temperature, name="get_temperature")
]
