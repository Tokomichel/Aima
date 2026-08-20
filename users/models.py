from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def check_password(self, raw_password):
        # Implement your password checking logic here
        return self.password == raw_password