from django.db import models
from django.contrib.auth.models import User

class Looser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.username
