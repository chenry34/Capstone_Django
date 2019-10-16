from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(unique=True)  # Primary Key
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_date = models.DateField()

