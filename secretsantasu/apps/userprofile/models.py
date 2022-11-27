from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # other fields here

    def __str__(self):
        return self.user.username
