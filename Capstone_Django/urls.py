from django.urls import path

from . import views

urlpatterns = [
    path('getTemperature', views.get_temperature, name="get_temperature"),
    path('setTemperature', views.set_temperature, name="set_temperature"),
    path('getHumidity', views.get_humidity, name="get_humidity"),
    path('setHumidity', views.set_humidity, name="set_humidity"),
    path('getMotion', views.get_motion_status, name="get_motion_status"),
    path('setMotion', views.set_motion_status, name="set_motion_status"),
    path('getWindow', views.get_window_status, name="get_window_status"),
    path('setWindow', views.set_window_status, name="set_window_status"),
    path('getDoor', views.get_door_status, name="get_door_status"),
    path('setDoor', views.set_door_status, name="set_door_status"),
    path('getLight', views.get_light_status, name="get_light_status"),
    path('getLightForArduino', views.get_light_for_arduino, name="get_light_for_arduino"),
    path('setLight', views.set_light_status, name="set_light_status"),
    path('getCO', views.get_co_status, name="get_co_status"),
    path('setCO', views.set_co_status, name="set_co_status"),
    path('createUser', views.create_user, name="create_user"),
    path('', views.index, name="index")
]
