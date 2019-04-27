from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

    # def is_staff(self):
    #     return self.is_staff == True or self.groups.filter(name__ends_with='Officers').exists()