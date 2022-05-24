from django.db import models


class User(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)