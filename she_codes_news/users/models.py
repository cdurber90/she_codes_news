from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    about = models.TextField(blank = True)
    user_img = models.URLField(blank = True)

    def __str__(self):
        return self.username

