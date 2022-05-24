from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return(f"{self.id}.{self.username} {self.password}")