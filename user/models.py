from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    