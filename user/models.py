import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class User(AbstractUser):
    middle_name = models.CharField(max_length=30, null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    registered_at = models.DateField(null=True,blank=True)
    last_login = models.TimeField(null=True,blank=True)
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     verbose_name='groups',
    #     related_name='custom_user_set',  # You can change this name
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     related_query_name='user'
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     verbose_name='user permissions',
    #     related_name='custom_user_set',  # You can change this name
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     related_query_name='user'
    # )
    def __str__(self):
        return self.first_name

    def was_recently_registered(self):
        return self.last_login >= timezone.now() - datetime.timedelta(days=1)
