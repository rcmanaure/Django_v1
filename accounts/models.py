from django.contrib.auth.models import AbstractUser
from django.db import models  # noqa


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email
