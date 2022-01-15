from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Equip(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    manufacturer = models.CharField(max_length=65)
    installer = models.TextField()
    inspector = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
