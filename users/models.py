from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    class Role(models.TextChoices):
        CUSTOMER = "customer", "Customer"
        SELLER = "seller", "Seller"

    role = models.CharField(max_length=50, choices=Role.choices)