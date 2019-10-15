from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, unique=True, db_column='USER_ID')
    user_name = models.CharField(max_length=255, db_column='USERNAME')
    password = models.CharField(max_length=255, db_column='PASS')
    created_date = models.DateField(db_column='CREATED_ON_DATETIME')

