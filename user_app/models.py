from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    user_avatar = models.ImageField(blank=True,null=True)
    user_phone = models.CharField(max_length=20)
    user_gender = models.BooleanField(blank=True,null=True)
    user_status = models.BooleanField(default=False)

    def __str__(self):
        return self.username
