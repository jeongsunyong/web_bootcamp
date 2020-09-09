from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=128,null=False, blank=False)
    intro = models.TextField(blank=True, null=False)
