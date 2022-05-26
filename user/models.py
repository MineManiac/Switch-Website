from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    # title = models.CharField(max_length=200)
    # content = models.TextField()
    friends = models.ManyToManyField("User", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    