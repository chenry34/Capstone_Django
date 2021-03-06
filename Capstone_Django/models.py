from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(unique=True, primary_key=True)  # Primary Key
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField()


class Temperature(models.Model):
    id = models.AutoField(unique=True, primary_key=True)  # Primary Key
    value = models.FloatField()
    time_stamp = models.DateTimeField()


class Humidity(models.Model):
    id = models.AutoField(unique=True, primary_key=True)  # Primary Key
    value = models.FloatField()
    time_stamp = models.DateTimeField()


class Window(models.Model):
    id = models.AutoField(unique=True, primary_key=True)  # Primary Key
    value = models.FloatField()
    time_stamp = models.DateTimeField()


class Door(models.Model):
    id = models.AutoField(unique=True, primary_key=True)  # Primary Key
    value = models.FloatField()
    time_stamp = models.DateTimeField()


class Motion(models.Model):
    id = models.AutoField(unique=True, primary_key=True)  # Primary Key
    value = models.FloatField()
    time_stamp = models.DateTimeField()


class CarbonMonoxide(models.Model):
    id = models.AutoField(unique=True, primary_key=True)  # Primary Key
    value = models.FloatField()
    time_stamp = models.DateTimeField()


class Light(models.Model):
    id = models.AutoField(unique=True, primary_key=True)  # Primary Key
    value = models.FloatField()
    time_stamp = models.DateTimeField()