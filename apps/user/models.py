from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    team = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
