from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    # title = models.CharField(max_length=200)
    # content = models.TextField()
    friends = models.ManyToManyField("User", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Friend_Request(models.Model):
    from_user = models.ForeignKey(
        User, related_name='from_ser', on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name = 'to_user', on_delete=models.CASCADE
    )
    