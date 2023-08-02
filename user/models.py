import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    user_name = models.CharField(max_length=30, null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, null=True)
    password_hash = models.CharField(max_length=32, null=True)
    registered_at = models.DateField(null=True)
    last_login = models.TimeField(null=True)

    def __str__(self):
        return self.first_name

    def was_recently_registered(self):
        return self.last_login >= timezone.now() - datetime.timedelta(days=1)
